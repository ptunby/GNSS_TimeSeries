import pandas as pd
import numpy as np
import glob
import fit_velocities, get_coordinates

def fit_all_velocities(folder, glob_pattern):
    """
    The function accepts a folder name and a 'glob' pattern and returns a pandas
    data frame with the site name, coordinates, velocities and uncertainties.
    It uses the modules 'fit_velocities' and 'get_coordinates'.
    param a: folder as a string
    param b: a 'glob' pattern that searches for the file of interest.
    returns: a pandas dataframe with the site name, coordinates, velocities, and uncertainties.
    """
    
    filename_list = []
    sitename_list = []
    csv_files = glob.glob(f"{folder}/{glob_pattern}")
    
    #Iterates through the glob and extracts the filename and stores in a list
    for i in csv_files:
        filename = i.split('\\')[-1]
        sitename = filename.split('/')[-1].split('.')[0]
        filename_list.append(filename)
        sitename_list.append(sitename)
    
    velocities = [fit_velocities.fit_velocities(file) for file in filename_list]
    coordinates = [get_coordinates.get_coordinates(file) for file in filename_list]
    
    #Create individual dataframes
    site_name = pd.DataFrame({'site name':sitename_list})
    veloc = pd.DataFrame(velocities)
    coord = pd.DataFrame(coordinates)
    
    new_df = pd.DataFrame(data = {'latitude': coord[0], 'longitude': coord[1], 'elevation': coord[2], 
                                  'east component velocity': veloc.iloc[:, 0].apply(lambda x: x[0]), 'north component velocity': veloc.iloc[:, 0].apply(lambda x: x[1]),
                                  'up component velocity': veloc.iloc[:, 0].apply(lambda x: x[2]),'east component uncertainty': veloc.iloc[:, 1].apply(lambda x: x[0]),
                                  'north component uncertainty': veloc.iloc[:, 1].apply(lambda x: x[1]), 'up component uncertainty': veloc.iloc[:, 1].apply(lambda x:x[2])})
    
    #Combine the dataframes
    final_df = pd.concat([site_name, new_df], axis = 1)
    
    return(final_df)