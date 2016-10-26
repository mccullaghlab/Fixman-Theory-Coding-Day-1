
import sys
import math
import numpy as np

inputFile = sys.argv[1]

# initialize loop variables
lineCount = 0
dataList = []

# open data file
f = open(inputFile)
# read file line by line
for line in f:
	step = line.split()[0]
	hbondDistance = float(line.split()[1])
	dataList.append(hbondDistance)
	lineCount += 1
# close file
f.close()

# convert to numpy array
dataList = np.asarray(dataList)
dataStdev = np.std(dataList)
dataAvg = np.mean(dataList)

# print information
print "Number of lines:", lineCount
print "Sum of hbond distances:", sum(dataList)
print "Average hbond distance:", dataAvg
print "Standard Deviation:", dataStdev

