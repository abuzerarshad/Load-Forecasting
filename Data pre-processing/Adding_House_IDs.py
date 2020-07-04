#import libraries
import pandas as pd
import glob

#directory path
path = 'E:/Research Workspace/Load-Forecasting/Dataset/PRECON'
allFiles = glob.glob(path + '/*.csv')

#Adding House_ID column to all the csv files in the directory
for filename in allFiles:
	df = pd.read_csv(filename)
	df.insert(0,'House_ID', filename.split('\\')[1].split(".")[0])
	df.to_csv(filename, index = False)