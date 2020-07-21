#import libraries
import pandas as pd
import glob
import os
import numpy as np

#directory path
path = 'C:/Users/abuzer.arshad/Desktop/precon-house-31-42'
os.chdir(path)

#Read CSV combined file for load
loadData = pd.read_csv('House7.csv')

#Read metadata file
metaData = pd.read_csv('Metadata.csv')
metaHeader = pd.read_csv('Metadata.csv', nrows = 1).columns
print(metaHeader)
print(metaData.loc[metaData.House_IDs == 'House7']['Property_Area_sqft'])

#iterate through metadata columns and insert into data files
for header in metaHeader:
	if header != 'House_IDs':
		loadData[header] = np.nan;
	
for House_IDs in metaData.itertuples():
	for House_ID in loadData.itertuples():
		if House_IDs == House_ID:
			print('hello')
			#loadData['Property_Area_sqft'] = row['Property_Area_sqft'] =  metaData.loc[metaData.House_IDs == row['House_ID']]['Property_Area_sqft']
			#loadData['Building_Year'] = row['Building_Year'] = metaData.loc[metaData.House_IDs == row['House_ID']]['Building_Year']
		
#export to csv
#loadData.to_csv( 'UpdatedHouse7.csv', index=False, encoding='utf-8-sig')