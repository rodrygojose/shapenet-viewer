# Gen configuration file for render all models of a directory with shapeNet viewer

from os import listdir
from os import path
import os 

DATABASE_PATH = "/user/rortizca/home/workspace/useful_code/shapenet-viewer/scripts"
CONFIG_FILE = "configFile.txt"

dirs = filter(os.path.isdir, os.listdir(DATABASE_PATH)) 
file = open( CONFIG_FILE,'w')

for dir in dirs:
  file.write( dir + ' n')

file.close()

