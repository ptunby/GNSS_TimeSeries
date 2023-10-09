import scipy.optimize
import numpy as np
import pandas as pd
import fit_timeseries

def fit_tide_gauge(filename):
    
    """
    This function takes a file name for a csv file and returns the estimated E, N and U components of velocity for that site
    It uses the module 'fit_timeseries'.
    using a linear least squares fit.
    param a: filename as a string
    returns: the estimated components of the velocities and uncertainties for the east, north, and up
    """
    
    #Data read into a pandas dataframe
    data = pd.read_csv(filename, sep = ';', names = ['year', 'mm', 'other', 'other2'])
    #Define the variables to pass to the fitting function
    year = data['year']
    mm = data['mm']
    
    vels,uncerts = fit_timeseries.fit_timeseries(year, mm)
    
    return vels, uncerts