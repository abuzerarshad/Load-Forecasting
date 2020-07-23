#import libraries
import pandas as pd
import glob
import os
import numpy as np
import re

#directory path
path = 'E:/Research Workspace/Load-Forecasting/Dataset/PRECON'
allFiles = glob.glob(path + '/*.csv')

#Read metadata file
metaData = pd.read_csv('E:/Research Workspace/Load-Forecasting/Dataset/Metadata.csv')
regex = re.compile("([a-zA-Z]+)([0-9]+)")

#Read CSV files for load
for filename in allFiles:
	#Read file name
	filenameOnly = filename.split('\\')[1].split(".")[0]
	
	#Get an index from the filename
	index = regex.match(filenameOnly)
	index = int(index.group(2))
	
	#Read CSV file and insert columns and values
	df = pd.read_csv(filename)
	df.insert(3,'Property_Area_sqft',metaData.at[index-1, 'Property_Area_sqft'])
	df.insert(4,'No_of_Floors',metaData.at[index-1,'No_of_Floors'])
	df.insert(5,'Building_Year',metaData.at[index-1,'Building_Year'])
	df.insert(6,'Ceiling_Height_ft',metaData.at[index-1,'Ceiling_Height_ft'])
	df.insert(7,'Ceiling_Insulation',metaData.at[index-1,'Ceiling_Insulation'])
	df.insert(8,'Total_No_of_Rooms',metaData.at[index-1,'Total_No_of_Rooms'])
	df.insert(9,'Bedrooms',metaData.at[index-1,'Bedrooms'])
	df.insert(10,'Livingrooms',metaData.at[index-1,'Livingrooms'])
	df.insert(11,'Drawingrooms',metaData.at[index-1,'Drawingrooms'])
	df.insert(12,'Kitchen',metaData.at[index-1,'Kitchen'])
	df.insert(13,'Connection_Type',metaData.at[index-1,'Connection_Type'])
	df.insert(14,'No_of_People',metaData.at[index-1,'No_of_People'])
	df.insert(15,'Adults_14_to_60',metaData.at[index-1,'Adults_14_to_60'])
	df.insert(16,'Children_0_to_13',metaData.at[index-1,'Children_0_to_13'])
	df.insert(17,'Seniors',metaData.at[index-1,'Seniors'])
	df.insert(18,'Permanent_Residents',metaData.at[index-1,'Permanent_Residents'])
	df.insert(19,'Temporary_Residents',metaData.at[index-1,'Temporary_Residents'])
	df.insert(20,'No_of_ACs',metaData.at[index-1,'No_of_ACs'])
	df.insert(21,'No_of_Refrigerators',metaData.at[index-1,'No_of_Refrigerators'])
	df.insert(22,'No_of_WashingMachines',metaData.at[index-1,'No_of_WashingMachines'])
	df.insert(23,'No_of_Electronic_Devices',metaData.at[index-1,'No_of_Electronic_Devices'])
	df.insert(24,'No_of_Fans',metaData.at[index-1,'No_of_Fans'])
	df.insert(25,'No_of_Water_Pumps',metaData.at[index-1,'No_of_Water_Pumps'])
	df.insert(26,'No_of_Electric_Heaters',metaData.at[index-1,'No_of_Electric_Heaters'])
	df.insert(27,'No_of_Irons',metaData.at[index-1,'No_of_Irons'])
	df.insert(28,'No_of_Lighting_Devices',metaData.at[index-1,'No_of_Lighting_Devices'])
	df.insert(29,'No_of_UPS',metaData.at[index-1,'No_of_UPS'])
		
	#export to csv
	df.to_csv(filename, index=False, encoding='utf-8-sig')