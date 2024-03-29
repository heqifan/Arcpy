# -- coding: utf-8 --
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


def Raster_Project(indir,outdir,character,resample_type,cellsize):
    arcpy.env.scratchWorkspace = indir
    env.workspace = indir
    List = arcpy.ListRasters(character)
    if len(List) == 0:
        return 0
    for data in List:
        # try:
        out_name = outdir + os.sep + "Resample_" + data[:-4] + '.tif'
        # (fname, fename) = os.path.splittext(out_name)
        if (os.path.exists(out_name)):
            print('exist,continue')
            continue
        else:
            print(data)
            arcpy.Resample_management(data, outdir + os.sep + 'Resample_' + data[:-4] + ".tif" , cellsize, resample_type)
            print(out_name)
        # except:
        #     # print(arcpy.GetMessages(2))
        #     print('{} is error continue'.format(data))
        #     continue
    return 1

# path = {r'F:\Integrated_analysis_data\Data\1Y\LAI_2003_2017_1y':'tif'}

resample_type = 'BILINEAR'


inpath = r'E:\Integrated_analysis_data\Data\1Y\MuSyQ_1981_2018_1y_chinese'

cellsize = 1000

styear = 1981
edyear = 2018

character = 'Mul*.tif'
for year  in range(styear,edyear+1):
    indir = inpath + os.sep + str(year)
    outdir = inpath + os.sep + str(year)
    Raster_Project(indir,outdir,character,resample_type,cellsize)
    print('{} is ok '.format(year))
print('{}  is ok !!!!!'.format(inpath))

# set workspace environment
# dirs = os.listdir( inpath )
# # 输出所有文件和文件夹
# for file in dirs:
#     dirpath = inpath + os.sep +  file
#     # set local variables
#     Raster_Project(dirpath, dirpath, '*.tif', prj_path, reproject_type,mask_data)
#     # print messages when the tool runs successfully
#     print(file + ' is ok!!!')

# indir = inpath
# outdir = indir
# Raster_Project(indir,outdir,character,prj_path,reproject_type,mask_data)
# print('{}  is ok !!!!!'.format(inpath))

