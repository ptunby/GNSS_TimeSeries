# GNSS_TimeSeries
These python modules were created to interact with GNSS timeseries data.
This data has relates to earthquake data that this module interacts with includes:
site name,  yyyy.yyyy (decimal year), velocities (north, east, and up), and uncertainty with the data.

## fit_timeseries
This module takes in two lists (time and a velocity) and returns a least-ssquares velocity and uncertainty for the timeseries.

## fit_velocities
This module accepts a filename and reads in GNSS data. The data is space separated. It then uses 'fit_timeseries' to return the east, north, and up components of velocity for the site.

## get_coordinates
This module accepts a filename and returns the average latitude, longitude, and elevation of the site for the timeperiod.

## fit_all_velocities
This module takes in a folder name, 'glob' pattern, and either a string (either 'GNSS' or 'tide') to specify the data to be analyed. It then returns a pandas dataframe with the site name, average coordinates, velocities, and uncertainties of all files that match the pattern for the 'GNSS' data and the site name, velocity, and uncertainties for the 'tide' data. This uses the 'fit_velocities', 'get_coordinates', and 'fit_tide_gauge' modules.

## fit_tide_gauge
This module takes in a file name for the decimal degrees and sea level change in mm and returns the estimated rate of change for that site and the
uncertainty of the fit. The data is separated by ';'.It uses the module 'fit_timeseries'. The data is from the website: https://psmsl.org/products/gloss/glossmap.html
