import scipy.optimize
import numpy as np

def fit_timeseries(tlist,ylist):
    """
    This function takes in an x and y value and performs a linear least squares fit.
    param a: x-value column array
    param b: y-value column array
    returns: least-squares velocity and uncertainty for the timeseries in given units
    
    """
    
    def my_line(x,a,b):
        return a + b * x
    
    m, mcov = scipy.optimize.curve_fit(my_line, tlist, ylist)
    uncerts = np.sqrt(np.diag(mcov))
    
    return(m[1], uncerts[1])