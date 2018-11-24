'''
Just a special file for benchmark data treatment
'''


#first let's get BENCHMARK video 
import numpy as np
import pandas as pd

filename = "smileBase-181124011003-pitch.csv"
readFile = pd.read_csv(filename)


#----checking stuff
#print(readFile.shape)
#print(readFile.columns)

#let's average out the values into a new dictionary
averages = {}
for col in readFile.columns:
	if col != 'Unnamed: 0':
		colStr = str(col)
		averages[col] = np.mean(np.array(readFile[str(col)]))

#----checking stuff
#print(averages)


# Save it as a benchmark csv to be compared @ indicoanalyze.py
df = pd.DataFrame(averages, index=[0])
csvName = filename[:-9]
newCsvName = csvName + "average.csv"
df.to_csv(newCsvName)

