#import libraries
import pandas as pd
import glob
import os

#directory path
path = 'E:/Research Workspace/Load-Forecasting/Dataset/PRECON'
os.chdir(path)

#Set Null values to zero
df = pd.read_csv('combinedLoadData.csv').fillna(value = 0)

#export to csv
df.to_csv( "combinedLoadData.csv", index=False, encoding='utf-8-sig')