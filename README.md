# GNSS_TimeSeries
These python modules were created to interact with GNSS timeseries data.
This data has relates to earthquake data that this module interacts with includes:
site name,  yyyy.yyyy (decimal year), velocities (north, east, and up), and uncertainty with the data.

## fit_timeseries
This module takes in two lists (time and a velocity) and returns a least-ssquares velocity and uncertainty for the timeseries.

## fit_velocities
This module accepts a filename and reads in GNSS data. It then uses 'fit_timeseries' to return the east, north, and up components of velocity for the site.

## get_coordinates
This module accepts a filename and returns the average latitude, longitude, and elevation of the site for the timeperiod.

## fit_all_velocities
This module takes in a folder name and 'glob' pattern that fits the files wanted in the folder. It then returns a pandas dataframe with the site name, average coordinates, velocities, and uncertainties of all files that match the pattern. This uses the 'fit_velocities' and 'get_coordinates' modules.
