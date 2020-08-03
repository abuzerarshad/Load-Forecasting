#import libraries
import pandas as pd
import glob

#directory path
path = 'E:/Research Workspace/Load-Forecasting/Dataset/PRECON'
allFiles = glob.glob(path + '/*.csv')

#count the number of columns in a load file
count = 0

#print filenames with exact 3 columns i.e. houseID, DateTime and Usage_Kwh
for filename in allFiles:
    df = pd.read_csv(filename)
    count = len(df.columns)
    if count == 30:
        print(filename.split('\\')[1].split(".")[0])