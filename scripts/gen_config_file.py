# Gen configuration file for render all models of a directory with shapeNet viewer

import os 

DATABASE_PATH_3D = "/run/media/rortizca/HD_Dell/rodrigo/ShapeNet_data/shapenet-models"
DATABASE_PATH_2D = "/run/media/rortizca/HD_Dell/rodrigo/ShapeNet_data/shapenet-renders/screenshots/models/3dw"
CONFIG_FILE   	 = "configFile.txt"

dirs_in 	= os.listdir( DATABASE_PATH_3D )
dirs_out 	= os.listdir( DATABASE_PATH_2D )

dirs 		= [name for name in dirs_in if name not in dirs_out ];

file = open( CONFIG_FILE,'w')
file.write("viewer.commands = [");

for dir in dirs:
  file.write("\"load " + dir + "\", \"save model screenshots\", ")

file.write("]");
file.close()

