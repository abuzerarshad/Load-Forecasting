#import libraries
import pandas as pd
import glob
import os

#directory path
path = 'E:/Research Workspace/Load-Forecasting/Dataset/PRECON'
os.chdir(path)

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(file) for file in all_filenames ])

#export to csv
combined_csv.to_csv( "combinedLoadData.csv", index=False, encoding='utf-8-sig')