import numpy as np
from numbers import Number


def save_dataset(ds, output_file="../test.nc"):
    """
    Attempts to save the dataset to a NetCDF file. If a TypeError occurs due to invalid attribute values,
    it converts the invalid attributes to strings and retries the save operation.

    Parameters
    ----------
    ds (xarray.Dataset): The dataset to be saved.
    output_file (str): The path to the output NetCDF file. Defaults to 'test.nc'.

    Returns
    -------
    bool: True if the dataset was saved successfully, False otherwise.

    Based on: https://github.com/pydata/xarray/issues/3743
    """
    valid_types = (str, int, float, np.float32, np.float64, np.int32, np.int64)
    # More general
    valid_types = (str, Number, np.ndarray, np.number, list, tuple)
    try:
        ds.to_netcdf(output_file, format="NETCDF4_CLASSIC")
        return True
    except TypeError as e:
        print(e.__class__.__name__, e)
        for varname, variable in ds.variables.items():
            for k, v in variable.attrs.items():
                if not isinstance(v, valid_types) or isinstance(v, bool):
                    print(
                        f"variable '{varname}': Converting attribute '{k}' with value '{v}' to string."
                    )
                    variable.attrs[k] = str(v)
        try:
            ds.to_netcdf(output_file, format="NETCDF4_CLASSIC")
            return True
        except Exception as e:
            print("Failed to save dataset:", e)
            datetime_vars = [
                var for var in ds.variables if ds[var].dtype == "datetime64[ns]"
            ]
            print("Variables with dtype datetime64[ns]:", datetime_vars)
            float_attrs = [
                attr for attr in ds.attrs if isinstance(ds.attrs[attr], float)
            ]
            print("Attributes with dtype float64:", float_attrs)
            return False
