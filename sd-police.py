# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 13:38:50 2019

@author: Eric Born
"""

import os
from sys import exit
from matplotlib import rcParams, pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_style("darkgrid")

# Set display options for dataframes
#pd.set_option('display.max_rows', 100)
#pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 50)


# setup input directory and filename
data = 'ripa_stops_datasd_v1'
input_dir = r'C:\Users\TomBrody\Desktop\Projects\police-violence'
ticker_file = os.path.join(input_dir, data + '.csv')

# read csv file into dataframe
try:
    police_df = pd.read_csv(ticker_file)
    print('opened file for police stops: ', data,'\n')

except Exception as e:
    print(e)
    exit('failed to read police data from: '+ str(data)+'.csv')
   
# remove ori and agency columns as data is the same for all rows
# removed intersection column as only 19 rows of data
police_df.drop(police_df.columns[[1, 2, 12]], axis = 1, inplace = True)

# describe the total rows and columns
print('The total length of the dataframe is', police_df.shape[0], 'rows',
      'and the width is', police_df.shape[1], 'columns')


# convert columns from numbers to words, 0 = no, 1 = yes
# (5)stop_in_response_to_cfs, (12)highway_exit, (18)isstudent, 
# (19)perceived_limited_english, (22)gender_nonconforming.

# perceived_gender - 1. Male, 2. Female, 3. Transgender man/boy, 
# 4. Transgender woman/girl, 5. Gender nonconforming 

# gend_nc - blank = no, 5 = yes
columns = [5, 12, 18, 19, 22]

police_df = police_df.iloc[:, columns].replace(0, value='no', inplace=True)

