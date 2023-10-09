import pandas as pd
import numpy as np
import fit_timeseries

def fit_velocities(filename):
    """
    This function takes a file name for a csv file and returns the estimated E, N and U components of velocity for that site
    It uses the module 'fit_timeseries'.
    using a linear least squares fit.
    param a: filename as a string
    returns: the estimated components of the velocities and uncertainties for the east, north, and up
    """
    
    #Data read into a pandas dataframe
    data = pd.read_csv(filename, delim_whitespace=True)
    #Define the variables to pass to the fitting function
    dec_year = data['yyyy.yyyy']
    east_m = data['__east(m)']
    north_m = data['_north(m)']
    up_m = data['____up(m)']
    
    #result = pd.DataFrame(columns = ['velocities', 'uncertainty'][1:3])
    vels=np.zeros((3,1))
    uncerts=np.zeros((3,1))
    n=0
    for i in [east_m, north_m, up_m]:
        vels[n],uncerts[n] = fit_timeseries.fit_timeseries(dec_year, i)
        n += 1
    
    return vels, uncerts