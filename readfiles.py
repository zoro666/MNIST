""" 
This script is used to perform preprocessing on data. 
""" 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import os
from argparse import ArgumentParser
import glob

parser = ArgumentParser()
parser.add_argument("-f","--file", help="input the filename", type = str)
args = parser.parse_args()
path = args.file
print(path)
data = pd.read_csv(path)
print(data.iloc[0])
# print(glob.glob('../Data'))