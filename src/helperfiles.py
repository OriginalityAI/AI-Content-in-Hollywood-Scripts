import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scienceplots

def get_data():
    """
    reads the individual datasets of the soaps, pilots, and SNL episode transcripts
    selects only relevant columns, filters through the 2020-2023 date range
    concats the datasets and saves the new file
    returns: the concatenated datasets
    """
    df_soap = pd.read_csv("../data/dataset_with_aicontent_soap.csv").drop(columns="Unnamed: 0")
#     df_pilot = pd.read_csv("../data/dataset_with_aicontent_pilot.csv")
    df_snl = pd.read_csv("../data/dataset_with_aicontent_snl.csv")
    
    df_soap.date = pd.to_datetime(df_soap.date)
    df_soap['year'] = df_soap.date.dt.year
#     df_pilot.year = df_pilot.year+1
    
#     df_pilot['genre']='Primetime Pilot'
    df_soap['genre']='Daytime Soap'
    df_snl['genre']='LateNight Comedy'
    
    dfs = []
    for df in [
#         df_pilot, 
        df_soap, 
        df_snl]:
        d = df.drop_duplicates()
        d = d[d.year>2019]
        dfs.append(d[['year', 'genre', 'aiContent']].dropna().copy()
                  )
    df = pd.concat(dfs)
    df.to_csv('../data/full_dataset.csv', index=False)
                 
    return df

def get_custom_cmap(col):
    """create my custom color map for plotting the pivot table"""
    from matplotlib.colors import LinearSegmentedColormap
    if col == 'aiContent':
        colors = [(0.8, 1, 1), (0.4, 1, 1)]
    if col == 'originalContent':
        colors = [(0, 0.4, 0.8), (0, 0, 0.8)]
    custom_cmap = LinearSegmentedColormap.from_list('cmap_blue', colors, N=256)
    return custom_cmap



