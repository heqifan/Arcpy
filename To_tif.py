<<<<<<< HEAD
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

path = r'E:\Yang\ET_data\AVHRR\ET_1982_1999\1982'
stuffix = 'hdf'

def to_tif(path,stuffix):
    arcpy.env.scratchWorkspace = path + os.sep
    env.workspace = path + os.sep
    List = arcpy.ListRasters('*.' +  stuffix)
    for i in List:
        try:
            arcpy.ExtractSubDataset_management(i, path  + os.sep + i[:-4] + '.tif')
        except:
            print('{} is error !!'.format(i))
            continue
    return 1



# dirs = os.listdir(path)
# for dir in dirs:
#     print(dir)
#     dir_path = path + os.sep + dir
#     to_tif(path,stuffix)
#     print('{}  is ok !!!!!'.format(dir))

=======
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

path = r'E:\Yang\ET_data\AVHRR\ET_1982_1999\1982'
stuffix = 'hdf'

def to_tif(path,stuffix):
    arcpy.env.scratchWorkspace = path + os.sep
    env.workspace = path + os.sep
    List = arcpy.ListRasters('*.' +  stuffix)
    for i in List:
        try:
            arcpy.ExtractSubDataset_management(i, path  + os.sep + i[:-4] + '.tif')
        except:
            print('{} is error !!'.format(i))
            continue
    return 1



# dirs = os.listdir(path)
# for dir in dirs:
#     print(dir)
#     dir_path = path + os.sep + dir
#     to_tif(path,stuffix)
#     print('{}  is ok !!!!!'.format(dir))

>>>>>>> 50a0148 (first commit)
to_tif(path,stuffix)