# importing the required modules
import glob
import pandas as pd

# specifying the path to csv files
path = "/home/anishjoshi/Desktop/tourist"

# csv files in the path
file_list = glob.glob(path + "/*.csv")

# list of excel files we want to merge.
# pd.read_excel(file_path) reads the
# excel data into pandas dataframe.
csv_list = []

for file in file_list:
	csv_list.append(pd.read_csv(file))

# concatenate all DataFrames in the list
# into a single DataFrame, returns new
# DataFrame.
csv_merged = pd.concat(csv_list, ignore_index=True)

# exports the dataframe into excel file
# with specified name.
csv_merged.to_csv('tourist_arrival.csv', index=False)
