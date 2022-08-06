<<<<<<< HEAD
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


def Raster_Project(indir,outdir,character,prj_path,reproject_type):
    arcpy.env.scratchWorkspace = indir + os.sep
    env.workspace = indir + os.sep
    List = arcpy.ListRasters(character)
    if len(List) == 0:
        return 0
    for data in List:
        try:
            arcpy.ProjectRaster_management(data, outdir + os.sep + "Reproject_" + data , prj_path, reproject_type )
        except:
            print('{} is error continue'.format(data))
            continue
    return 1

path = {r'F:\Integrated_analysis_data\Data\1Y\LAI_2003_2017_1y':'tif'}


prj_path  = r'F:\Integrated_analysis_data\Data\prj\WGS_1984_Albers.prj'

reproject_type = 'BILINEAR'

styear = 2003
edyear = 2017

for inpath in path:
    print(inpath)
    character = 'Mul_*.' + path[inpath]
    for year  in range(styear,edyear+1):
        indir = inpath + os.sep + str(year)
        outdir = indir
        Raster_Project(indir,outdir,character,prj_path,reproject_type)
        print('{} is ok '.format(year))
    print('{}  is ok !!!!!'.format(inpath))
=======
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


def Raster_Project(indir,outdir,character,prj_path,reproject_type):
    arcpy.env.scratchWorkspace = indir + os.sep
    env.workspace = indir + os.sep
    List = arcpy.ListRasters(character)
    if len(List) == 0:
        return 0
    for data in List:
        try:
            arcpy.ProjectRaster_management(data, outdir + os.sep + "Reproject_" + data , prj_path, reproject_type )
        except:
            print('{} is error continue'.format(data))
            continue
    return 1

path = {r'F:\Integrated_analysis_data\Data\1Y\LAI_2003_2017_1y':'tif'}


prj_path  = r'F:\Integrated_analysis_data\Data\prj\WGS_1984_Albers.prj'

reproject_type = 'BILINEAR'

styear = 2003
edyear = 2017

for inpath in path:
    print(inpath)
    character = 'Mul_*.' + path[inpath]
    for year  in range(styear,edyear+1):
        indir = inpath + os.sep + str(year)
        outdir = indir
        Raster_Project(indir,outdir,character,prj_path,reproject_type)
        print('{} is ok '.format(year))
    print('{}  is ok !!!!!'.format(inpath))
>>>>>>> 50a0148 (first commit)
print('all is ok !!!!!!')