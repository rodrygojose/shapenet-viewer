# Gen configuration file for render all models of a directory with shapeNet viewer

import os 

DATABASE_PATH = "D:/D_workspace/database/shapenet-models"
CONFIG_FILE   = "configFile.txt"

dirs = os.listdir( DATABASE_PATH )

file = open( CONFIG_FILE,'w')
file.write("viewer.commands = [");

for dir in dirs:
  file.write("\"load " + dir + "\", \"save model screenshots\", ")

file.write("]");
file.close()

