
# -*- coding:utf-8 _*-
import arcpy
from arcpy.sa import *
from arcpy import Raster, ListRasters, Delete_management
import os
arcpy.gp.overwriteOutput = 1              #允许覆盖
arcpy.CheckOutExtension("Spatial")
from arcpy import env
env.workspace =  r'D:\sort_mask_out'
outpath = r'D:\sort_mask_out'
table_path = r'D:\TABLE_out'
rasters = arcpy.ListRasters("*")
shp_ = r'D:\duchang\duchang_project.shp'
for raster in rasters:
    print(raster)
    outTable = table_path + os.sep + raster.split('-')[0] + '_' + raster.split('-')[1] + '_' + raster.split('-')[2][:-4] + '.xls'
    print(outTable)
    outZSaT = ZonalStatisticsAsTable(shp_, 'FID', raster,outTable, "", "SUM")
    print outTable + "  is ok!!!!!"
print  "all is ok!!!!!!!!!!!"



