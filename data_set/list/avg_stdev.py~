
# load libraries
import sys
import math

# input file is first command line argument
inputFile = sys.argv[1]

# initialize loop variables
lineCount = 0
dataList = []

# open data file
f = open(inputFile)
# read data file line by line
for line in f:
	step = line.split()[0]
	hbondDistance = float(line.split()[1])
	dataList.append(hbondDistance)
	lineCount += 1
# close data file
f.close()

# average the data
dataAvg = sum(dataList) / lineCount

# print output
print "Number of lines:", lineCount
print "Sum of hbond distances:", sum(dataList)
print "Average hbond distance:", dataAvg

# compute standard deviation
dataStdev = 0.0
for i in range(lineCount):
	hbondDistance = dataList[i]
	temp = hbondDistance - dataAvg
	dataStdev += temp * temp

# print standard deviation
print "Standard Deviation:", math.sqrt(dataStdev/lineCount)

