
# load libraries
import sys
import math
import numpy as np

pi = 3.1415926535
degToRad = pi/180.0

# read xyz file
def read_xyz(xyzFile):
	global atomNames
	# open the file
	f = open(xyzFile)
	# initialize counters
	lineCount = 0
	atomCount = 0
	atomNames = []
	# read each line of the file
	for line in f:
		# number of atoms is printed on first line of XYZ file format
		if lineCount==0:
			nAtoms = float(line)
			positions = np.empty((nAtoms,3),dtype=float)
		# positions are after second line
		elif lineCount > 1:
			atomNames.append(line.split()[0])
			for k in range(3):
				positions[atomCount,k] = float(line.split()[k+1])
			atomCount += 1

		lineCount += 1
	f.close()
	# send the number of atoms and positions back. positions are numpy array
	return atomCount, positions

# write xyz file
def write_xyz(positions,xyzFile):
	global atomNames
	# determine number of atoms as size of first dimension of position array
	nAtoms = positions.shape[0]
	# open file for writing
	out = open(xyzFile,"w")
	# write number of atoms in first line of XYZ
	out.write("%10d\n" % (nAtoms))
	out.write("Translated Molecule\n")
	# loop through atoms and print atom positions and names
	for atom in range(nAtoms):
		out.write("%5s %10.5f %10.5f %10.5f\n" % (atomNames[atom], positions[atom,0], positions[atom,1], positions[atom,2]))
	out.close()

# rotate a set of three dimensional coordinates around the x axis by theta
def rot_x(positions,theta):
	# determine number of atoms as size of first dimension of position array
	nAtoms = positions.shape[0]

	# populate rotation matrix
	rot = np.zeros((3,3),dtype=float)
	rot[0,0] = 1.0
	rot[1,1] = math.cos(theta)
	rot[1,2] = -math.sin(theta)
	rot[2,1] = math.sin(theta)
	rot[2,2] = math.cos(theta)

	# perform rotation
	positions = np.dot(positions,rot)

	# return rotated positions
	return positions

# rotate a set of three dimensional coordinates around the y axis by theta
def rot_y(positions,theta):
	# determine number of atoms as size of first dimension of position array
	nAtoms = positions.shape[0]

	# populate rotation matrix
	rot = np.zeros((3,3),dtype=float)
	rot[1,1] = 1.0
	rot[0,0] = math.cos(theta)
	rot[0,2] = math.sin(theta)
	rot[2,0] = -math.sin(theta)
	rot[2,2] = math.cos(theta)

	# perform rotation
	positions = np.dot(positions,rot)

	# return rotated positions
	return positions

# rotate a set of three dimensional coordinates around the z axis by theta
def rot_z(positions,theta):
	# determine number of atoms as size of first dimension of position array
	nAtoms = positions.shape[0]

	# populate rotation matrix
	rot = np.zeros((3,3),dtype=float)
	rot[2,2] = 1.0
	rot[0,0] = math.cos(theta)
	rot[0,1] = -math.sin(theta)
	rot[1,0] = math.sin(theta)
	rot[1,1] = math.cos(theta)

	# perform rotation
	positions = np.dot(positions,rot)

	# return rotated positions
	return positions

#####################################################################################################################
###################################              MAIN PROGRAM           #############################################
#####################################################################################################################


xyzInputFile = sys.argv[1]
xyzOutputFile = sys.argv[2]
# read in rotation angle in degrees and convert immediately to radians
rotTheta = float(sys.argv[3]) * degToRad

# read atom positions
nAtoms, atomPositions = read_xyz(xyzInputFile)

# rotate
atomPositions = rot_x(atomPositions,rotTheta)
atomPositions = rot_y(atomPositions,rotTheta)
atomPositions = rot_z(atomPositions,rotTheta)

# write new atom positions
write_xyz(atomPositions,xyzOutputFile)



