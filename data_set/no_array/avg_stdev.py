# import libraries
import sys
import math

# read input file as first command line argument
inputFile = sys.argv[1]

# initialize loop variables
dataSum = 0.0
lineCount = 0

# open data file
f = open(inputFile)
# read data file line by line
for line in f:
	step = line.split()[0]
	hbondDistance = line.split()[1]
	# add to the data sum
	dataSum = dataSum + float(hbondDistance)
	# add one to line count (to count the number of lines)
	lineCount += 1
# close data file
f.close()
# average data
dataAvg = dataSum / lineCount
# print important information
print "Number of lines:", lineCount
print "Sum of hbond distances:", dataSum
print "Average hbond distance:", dataSum / lineCount

# compute standard deviation
dataStdev = 0.0
# open data file again
f = open(inputFile)
for line in f:
	hbondDistance = float(line.split()[1])
	temp = hbondDistance - dataAvg
	dataStdev += temp * temp
# close file
f.close()
# print standard deviation
print "Standard Deviation:", math.sqrt(dataStdev/lineCount)

