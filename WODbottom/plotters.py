import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from matplotlib.colors import BoundaryNorm
from netCDF4 import Dataset
from pandas import DataFrame


def plot_bathy_and_argo(ds_bathy, ds_bin=None, ds_interp=None):
    import warnings

    # Check if ds_bin or ds_interp have the variable WATER_DEPTH
    if ds_bin is not None and "WATER_DEPTH" not in ds_bin:
        warnings.warn("ds_bin does not contain the variable 'WATER_DEPTH'.")
    if ds_interp is not None and "WATER_DEPTH" not in ds_interp:
        warnings.warn("ds_interp does not contain the variable 'WATER_DEPTH'.")

    # Plot bathymetry and scatter Argo data colored by WATER_DEPTH
    fig, ax = plt.subplots(figsize=(12, 8))

    # Define levels and norm for bathymetry
    levels = np.arange(-5000, 0, 500)
    norm = BoundaryNorm(levels, ncolors=plt.cm.Blues.N, clip=True)

    # Plot bathymetry
    bathy = ax.contourf(
        ds_bathy["LONGITUDE"],
        ds_bathy["LATITUDE"],
        ds_bathy["TOPO"],
        levels=levels,
        cmap="Blues",
        norm=norm,
    )

    # Add colorbar for bathymetry
    cbar = plt.colorbar(
        bathy, ax=ax, orientation="vertical", pad=0.02, label="Depth (m)"
    )

    # Add labeled contour lines in dashed grey
    contour_lines = ax.contour(
        ds_bathy["LONGITUDE"],
        ds_bathy["LATITUDE"],
        ds_bathy["TOPO"],
        levels=levels,
        colors="grey",
        linestyles="dashed",
    )
    ax.clabel(contour_lines, inline=True, fontsize=8, fmt="%d")

    # Scatter Argo data colored by WATER_DEPTH
    if ds_interp is not None and "WATER_DEPTH" in ds_interp:
        ax.scatter(
            ds_interp["LONGITUDE"],
            ds_interp["LATITUDE"],
            c=ds_interp["WATER_DEPTH"],
            cmap="Blues",
            norm=norm,
            edgecolor="black",
            s=20,
            label="Argo Data",
        )

    if ds_bin is not None and "WATER_DEPTH" in ds_bin:
        ax.scatter(
            ds_bin["LONGITUDE"],
            ds_bin["LATITUDE"],
            c=ds_bin["WATER_DEPTH"],
            cmap="Blues",
            norm=norm,
            edgecolor="black",
            s=20,
            label="Binned Argo Data",
        )

    # Add title and labels
    ax.set_title("Bathymetry and Argo Data Colored by Water Depth", fontsize=14)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.legend(loc="upper right")

    plt.show()


def plot_bathymetry(ds_bathy):
    """
    Plots a simple bathymetry map using the provided bathymetry dataset.

    Parameters:
    ds_bathy (xarray.Dataset): The bathymetry dataset containing 'LONGITUDE', 'LATITUDE', and 'TOPO' variables.
    """
    # Define levels for the discrete colorbar
    levels = np.arange(-6000, 500, 500)
    norm = BoundaryNorm(levels, ncolors=plt.cm.Blues.N, clip=True)

    # Create a simple map of bathymetry using contourf
    plt.figure(figsize=(10, 8))
    contour = plt.contourf(
        ds_bathy["LONGITUDE"],
        ds_bathy["LATITUDE"],
        ds_bathy["TOPO"],
        levels=levels,
        cmap="Blues",
        norm=norm,
    )
    cbar = plt.colorbar(contour, ticks=levels, label="Depth (m)")
    plt.title("Simple Bathymetry Map")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.show()


##------------------------------------------------------------------------------------
## Views of the ds or nc file
##------------------------------------------------------------------------------------
def show_contents(data, content_type="variables"):
    """
    Wrapper function to show contents of an xarray Dataset or a netCDF file.

    Parameters:
    data (str or xr.Dataset): The input data, either a file path to a netCDF file or an xarray Dataset.
    content_type (str): The type of content to show, either 'variables' (or 'vars') or 'attributes' (or 'attrs'). Default is 'variables'.

    Returns:
    pandas.io.formats.style.Styler or pandas.DataFrame: A styled DataFrame with details about the variables or attributes.
    """
    if content_type in ["variables", "vars"]:
        if isinstance(data, str):
            return show_variables(data)
        elif isinstance(data, xr.Dataset):
            return show_variables(data)
        else:
            raise TypeError("Input data must be a file path (str) or an xarray Dataset")
    elif content_type in ["attributes", "attrs"]:
        if isinstance(data, str):
            return show_attributes(data)
        elif isinstance(data, xr.Dataset):
            return show_attributes(data)
        else:
            raise TypeError("Attributes can only be shown for netCDF files (str)")
    else:
        raise ValueError(
            "content_type must be either 'variables' (or 'vars') or 'attributes' (or 'attrs')"
        )


def show_variables(data):
    """
    Processes an xarray Dataset or a netCDF file, extracts variable information,
    and returns a styled DataFrame with details about the variables.

    Parameters:
    data (str or xr.Dataset): The input data, either a file path to a netCDF file or an xarray Dataset.

    Returns:
    pandas.io.formats.style.Styler: A styled DataFrame containing the following columns:
        - dims: The dimension of the variable (or "string" if it is a string type).
        - name: The name of the variable.
        - units: The units of the variable (if available).
        - comment: Any additional comments about the variable (if available).
    """
    from pandas import DataFrame
    from netCDF4 import Dataset

    if isinstance(data, str):
        print("information is based on file: {}".format(data))
        dataset = Dataset(data)
        variables = dataset.variables
    elif isinstance(data, xr.Dataset):
        print("information is based on xarray Dataset")
        variables = data.variables
    else:
        raise TypeError("Input data must be a file path (str) or an xarray Dataset")

    info = {}
    for i, key in enumerate(variables):
        var = variables[key]
        if isinstance(data, str):
            dims = var.dimensions[0] if len(var.dimensions) == 1 else "string"
            units = "" if not hasattr(var, "units") else var.units
            comment = "" if not hasattr(var, "comment") else var.comment
        else:
            dims = var.dims[0] if len(var.dims) == 1 else "string"
            units = var.attrs.get("units", "")
            comment = var.attrs.get("comment", "")

        info[i] = {
            "name": key,
            "dims": dims,
            "units": units,
            "comment": comment,
            "standard_name": var.attrs.get("standard_name", ""),
            "dtype": str(var.dtype) if isinstance(data, str) else str(var.data.dtype),
        }

    vars = DataFrame(info).T

    dim = vars.dims
    dim[dim.str.startswith("str")] = "string"
    vars["dims"] = dim

    vars = (
        vars.sort_values(["dims", "name"])
        .reset_index(drop=True)
        .loc[:, ["dims", "name", "units", "comment", "standard_name", "dtype"]]
        .set_index("name")
        .style
    )

    return vars


def show_attributes(data):
    """
    Processes an xarray Dataset or a netCDF file, extracts attribute information,
    and returns a DataFrame with details about the attributes.

    Parameters:
    data (str or xr.Dataset): The input data, either a file path to a netCDF file or an xarray Dataset.

    Returns:
    pandas.DataFrame: A DataFrame containing the following columns:
        - Attribute: The name of the attribute.
        - Value: The value of the attribute.
    """

    if isinstance(data, str):
        print("information is based on file: {}".format(data))
        rootgrp = Dataset(data, "r", format="NETCDF4")
        attributes = rootgrp.ncattrs()
        get_attr = lambda key: getattr(rootgrp, key)
    elif isinstance(data, xr.Dataset):
        print("information is based on xarray Dataset")
        attributes = data.attrs.keys()
        get_attr = lambda key: data.attrs[key]
    else:
        raise TypeError("Input data must be a file path (str) or an xarray Dataset")

    info = {}
    for i, key in enumerate(attributes):
        dtype = type(get_attr(key)).__name__
        info[i] = {"Attribute": key, "Value": get_attr(key), "DType": dtype}

    attrs = DataFrame(info).T

    return attrs


def show_variables_by_dimension(data, dimension_name="trajectory"):
    """
    Processes an xarray Dataset or a netCDF file, extracts variable information,
    and returns a styled DataFrame with details about the variables filtered by a specific dimension.

    Parameters:
    data (str or xr.Dataset): The input data, either a file path to a netCDF file or an xarray Dataset.
    dimension_name (str): The name of the dimension to filter variables by.

    Returns:
    pandas.io.formats.style.Styler: A styled DataFrame containing the following columns:
        - dims: The dimension of the variable (or "string" if it is a string type).
        - name: The name of the variable.
        - units: The units of the variable (if available).
        - comment: Any additional comments about the variable (if available).
    """

    if isinstance(data, str):
        print("information is based on file: {}".format(data))
        dataset = Dataset(data)
        variables = dataset.variables
    elif isinstance(data, xr.Dataset):
        print("information is based on xarray Dataset")
        variables = data.variables
    else:
        raise TypeError("Input data must be a file path (str) or an xarray Dataset")

    info = {}
    for i, key in enumerate(variables):
        var = variables[key]
        if isinstance(data, str):
            dims = var.dimensions[0] if len(var.dimensions) == 1 else "string"
            units = "" if not hasattr(var, "units") else var.units
            comment = "" if not hasattr(var, "comment") else var.comment
        else:
            dims = var.dims[0] if len(var.dims) == 1 else "string"
            units = var.attrs.get("units", "")
            comment = var.attrs.get("comment", "")

        if dims == dimension_name:
            info[i] = {
                "name": key,
                "dims": dims,
                "units": units,
                "comment": comment,
            }

    vars = DataFrame(info).T

    dim = vars.dims
    dim[dim.str.startswith("str")] = "string"
    vars["dims"] = dim

    vars = (
        vars.sort_values(["dims", "name"])
        .reset_index(drop=True)
        .loc[:, ["dims", "name", "units", "comment"]]
        .set_index("name")
        .style
    )

    return vars
