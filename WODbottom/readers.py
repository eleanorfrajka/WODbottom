import numpy as np
import xarray as xr

import bathyreq


def load_bathymetry(lonlim, latlim, dx=2, dy=1):
    """
    Load bathymetry data for a specified region.

    Parameters:
    lonlim (tuple): Longitude limits as (min_lon, max_lon).
    latlim (tuple): Latitude limits as (min_lat, max_lat).
    dx (int, optional): Longitude buffer. Default is 2.
    dy (int, optional): Latitude buffer. Default is 1.

    Returns:
    xr.Dataset: Bathymetry dataset.
    """
    req = bathyreq.BathyRequest()
    data, lonvec, latvec = req.get_area(
        longitude=[lonlim[0] - dx, lonlim[1] + dx],
        latitude=[latlim[0] - dy, latlim[1] + dy],
        size=[200, 201],
    )
    # Create an xarray dataset
    ds_bathy = xr.Dataset(
        {"TOPO": (["LATITUDE", "LONGITUDE"], np.flipud(data))},
        coords={"LONGITUDE": lonvec, "LATITUDE": latvec},
    )
    return ds_bathy
