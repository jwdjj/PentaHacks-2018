
import numpy as np
import pandas as pd

#read BENCHMARK average file
filename = "smileBase-181124011003-average.csv"
benchFile = pd.read_csv(filename)


#Also get user's data
filename2 = "tester-181124012054-pitch.csv"
userFile = pd.read_csv(filename2)

totalRow = userFile.shape[0]

# individual pie chart: find the maximum of each frame, percentage of each emotion 
pieDict = {}
for col in (pd.DataFrame(userFile).drop(columns='Unnamed: 0')).idxmax(axis=1):
	if col in pieDict:
		pieDict[col] = pieDict[col] + 1
	else:
		pieDict[col] = 1

#convert into percentage
for keys in pieDict:
	pieDict[keys] = (pieDict.get(keys)/totalRow)*100

#save into csv
df = pd.DataFrame(pieDict, index=[0])
csvName = filename2[:-22]
newCsvName = csvName + "piechart.csv"
#print(newCsvName)
df.to_csv(newCsvName)


#A dictionary that counts how many are ABOVE or BELOW average - comparison bar chart
overDict = {}
underDict = {}

for col in benchFile.columns[1:]:
	overDict[col] = ((userFile[col]>benchFile[col][0]).sum())
	underDict[col] = (((userFile[col]<benchFile[col][0])).sum())

#only plot the larger of the two (over/under) vs BENCHMARK average
#e.g 72% of the time you are more expressive than the benchmark. Good! :D
higherDict = {}
lowerDict = {}
for col in overDict:
	if((max(overDict.get(col),underDict.get(col)) == overDict.get(col))):
		higherDict[col] = (overDict.get(col)/totalRow)*100
	else:
		lowerDict[col] = (underDict.get(col)/totalRow)*100

benchAveDict = {}
for col in benchFile.columns[1:]:
	benchAveDict[col] = (benchFile[col][0])*100

#save into csv
df1 = pd.DataFrame(benchAveDict,index=["Benchmark Average"])
df2 = pd.DataFrame(higherDict,index=["Higher"])
df3 = pd.DataFrame(lowerDict,index=["Lower"])

frames = [df1,df2,df3]

result = pd.concat(frames)

newCsvName = csvName + "barchart.csv"
result.to_csv(newCsvName)


# line chart per frame comparison
# hii if you see this I think I don't need to make separate csv file for this
# (e.g just plot each column from tester.csv and from benchmark.csv on the same graph)



# Append average (the piechart data) to a masterfile
# !! NOT REALLY TESTED THAT WELL SINCE NEED UNIQUE DATA AND EXISTING master.csv
keyName = filename2[:-10]
newEntry = pd.DataFrame(pieDict,index=[keyName])

pd.read_csv('master.csv').append(newEntry).drop_duplicates().to_csv('master.csv')














