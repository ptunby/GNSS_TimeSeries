import os
import pandas as pd
import numpy as np

def get_coordinates(filename):
    """
    This function takes in a filename and outputs the average latitude, longitude, 
    and elevation for that site over the time period.
    param a: filename as a string
    returns: the average latitude, longitude, and elevation for the dataset timeperiod
    """
    
    #Data read into a pandas dataframe
    data = pd.read_csv(filename, delim_whitespace=True)
    
    avg_lat = np.average(data['_latitude(deg)'])
    avg_long = np.average(data['_longitude(deg)'])
    avg_elev = np.average(data['__height(m)'])
    
    return(avg_lat, avg_long, avg_elev)