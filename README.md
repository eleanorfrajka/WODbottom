# WODbottom

Extracting bottom temperature and salinity from World Ocean Database profiles.

- Select geographic region (40-90W, 26-55N), CTD and Profiling floats only 
- Choose individual profiles in netCDF format (not ragged)

- Wait for the data to be ready then download the two `*.tar` files (one for CTD and one for floats).


- Load the data.  For my region, there were around 213,000 files to be loaded
- Extract the temperature and salinity at the deepest (maximum z) location
- (Should also extract flag data... I chose WODflags)


Then compare to GEBCO bathymetry.  If the maxz is within 50m of the bottom then retain the T, S values.



