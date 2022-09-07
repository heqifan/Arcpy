# -- coding: utf-8 --
import arcpy
import os
from arcpy.sa import *
import os
arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

# Name: DefineProjection.py
# Description: Records the coordinate system information for the specified input dataset or feature class

inpath = r'J:\out_netcdf\out'
# set workspace environment
dirs = os.listdir( inpath )
sample_tif = r'E:\watershed\QinghaiLake_Admin_Boundary.shp'
# 输出所有文件和文件夹
for file in dirs:
    dirpath = inpath + os.sep +  file
    arcpy.env.workspace = dirpath
    arcpy.env.scratchWorkspace = dirpath
    List = arcpy.ListRasters('*.tif')
    for tif in List:
        try:
            # set local variables
            in_dataset = tif  # "forest.shp"

            # get the coordinate system by describing a feature class
            dsc = arcpy.Describe(sample_tif)
            coord_sys = dsc.spatialReference

            # run the tool
            arcpy.DefineProjection_management(in_dataset, coord_sys)
            # print messages when the tool runs successfully
            print(arcpy.GetMessages(0))

        except arcpy.ExecuteError:
            print(arcpy.GetMessages(2))

        except Exception as ex:
            print(ex.args[0])
    print(file + ' is ok!!!')