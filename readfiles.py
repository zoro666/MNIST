""" 
@Author : Zoro
This script is used to read data from a given file. 
""" 
# Laod all the libraries
import numpy as np 
import pandas as pd 
import tkinter
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import pickle

def load(path, filename, verbose = False):
	"""
	Load the data from the csv file 
	"""
	# Load the csv file
	data = pd.read_csv(path + filename)
	# Find the total number of samples
	nsamples,_ = data.shape
	# row and col sizes of given image data from 
	# data description found on the kaggle
	# digit-recognizer competition
	row = col = 28 			
	# Separate image matrices(X) and labels(Y) from the data
	X = np.zeros([row,col,nsamples]) 
	Y = np.zeros([nsamples,])
	# Extract pixel information from data to image matrices
	for sample in range(nsamples):
		if verbose:
			print("Extracting {} sample from data".format(sample))
		for i in range(row):
			for j in range(col):
				x = (i*28) + (j+1) 	# Given by the data description
				# Pixel information starts from second column
				X[i,j,sample] = data.iloc[sample,x]
				# Labels are present in first column(0th in python)
				Y[sample,] = data.iloc[sample,0]
	return X, Y

def save(path, filename, X, Y):
	"""
	Save the extracted information in pickeled format
	"""
	# Remove current extension from filename and add .sav extension
	filename = filename[:-4] + '.sav'
	# Save the image data
	pickle.dump(X, open(path + 'x_' + filename, 'wb'))
	# Save the labels
	pickle.dump(Y, open(path + 'y_' + filename, 'wb'))

def main(path,filename,Save,Display,VERBOSE,image_num=0):
	X, Y = load(path, filename,verbose = VERBOSE)
	if Save:
		# Save the files
		save(path, filename, X, Y)
		
	if Display:
		# Print the label of the image number
		print(Y[image_num]) 
		# Display the image for the given image number
		plt.imshow(X[:,:,image_num], cmap='gray')
		plt.show()

if __name__ == "__main__":
	# Read the filepath for csv files from command line
	parser = ArgumentParser()
	# First input path where files are stored
	parser.add_argument("-p","--path", help="input the filepath", type = str)
	# Second input filename
	parser.add_argument("-f","--file", help="input the filename", type = str)
	args = parser.parse_args()
	path = args.path
	filename = args.file
	# Execute main
	main(path,filename,Save = True,Display = False, VERBOSE = True, image_num=0)