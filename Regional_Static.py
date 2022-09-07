
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/27 17:36
# @Author : Xihuang O.Y.
import arcpy, os
from arcpy import sa
from arcpy.sa import *
from arcpy import env

arcpy.CheckOutExtension(r'Spatial')
arcpy.env.overwriteOutput = True


tifPath = [r'J:\Integrated_analysis_data\Data\1Y\Geodata_1982_2018_1y/',
           r'J:\Integrated_analysis_data\Data\1Y\GLASS_1982_2018_1y/',
           r'J:\Integrated_analysis_data\Data\1Y\W_1982_2018_1y/']

keys = [r'Mul_',r'Mul_',r'Resample_']

Region = [r'J:\Integrated_analysis_data\Data\shp\QTPshp\Merge.shp']

joinID = [r'name']

out_Path = r'E:\Wang_NPP_Region_Statical'

startY = 1982
endY = 2018

for shpi in range(0, len(Region)):
    for cla in range(0, len(tifPath)):
        # env.workspace = tifPath[cla]
        # tiffiles = arcpy.ListFiles( tifPath[cla] + keys[cla] + '*.tif')
        tiffiles = arcpy.ListRasters(tifPath[cla] + keys[cla] + '*.tif')
        print('Process_Data have  :',tiffiles)
        tiffiles.sort()
        print(tiffiles)
        for filename,yr in zip(tiffiles,range(startY,endY+1)):
            ULC = env.workspace + os.sep + filename
            field = keys[cla].split(r'_')[0]  + r'_' + str(yr)
            tempTable = out_Path + os.sep + field
            print(tempTable)
            arcpy.gp.ZonalStatisticsAsTable(Region[shpi], joinID[shpi], ULC, tempTable, 'DATA', 'MEAN')
            arcpy.AddField_management(tempTable, field, 'DOUBLE')
            arcpy.CalculateField_management(tempTable, field, '[MEAN]', 'VB', '')
            arcpy.JoinField_management(Region[shpi], joinID[shpi], tempTable, joinID[shpi], [field])


