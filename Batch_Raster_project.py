
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


def Raster_Project(indir,outdir,character,prj_path,reproject_type,mask_data):
    arcpy.env.scratchWorkspace = indir
    env.workspace = indir

    List = arcpy.ListRasters(character)
    if len(List) == 0:
        return 0
    for data in List:
        try:
            arcpy.ProjectRaster_management(data, outdir + os.sep + "Reproject_" + data[:-4] + '.tif', prj_path, reproject_type,'1000')
            arcpy.env.snapRaster = mask_data  # snap栅格
            arcpy.env.extent = mask_data  # 像元行列号一致
            outExtractByMask = ExtractByMask(outdir + os.sep + "Reproject_" + data[:-4] + '.tif', mask_data)
            outExtractByMask.save(outdir + os.sep + 'Mask_' + data[:-4] + '.tif')
            print(arcpy.GetMessages(0))
        except:
            print(arcpy.GetMessages(2))
            print('{} is error continue'.format(data))
            continue
    return 1

# path = {r'F:\Integrated_analysis_data\Data\1Y\LAI_2003_2017_1y':'tif'}


prj_path  = r'J:\Integrated_analysis_data\Data\prj\WGS_1984_Albers.prj'

reproject_type = 'BILINEAR'

mask_data = r'J:\Integrated_analysis_data\Data\Sample\Mask_Mul_2005.tif'

inpath = r'J:\Integrated_analysis_data\Data\8D\GLASS_1982_2018_8d\2018'


styear = 2018
edyear = 2018

character = 'A*.tif'
# for year  in range(styear,edyear+1):
#     indir = inpath + os.sep + str(year)
#     outdir = indir
#     Raster_Project(indir,outdir,character,prj_path,reproject_type,mask_data)
#     print('{} is ok '.format(year))
# print('{}  is ok !!!!!'.format(inpath))

# set workspace environment
# dirs = os.listdir( inpath )
# # 输出所有文件和文件夹
# for file in dirs:
#     dirpath = inpath + os.sep +  file
#     # set local variables
#     Raster_Project(dirpath, dirpath, '*.tif', prj_path, reproject_type,mask_data)
#     # print messages when the tool runs successfully
#     print(file + ' is ok!!!')

indir = inpath
outdir = indir
Raster_Project(indir,outdir,character,prj_path,reproject_type,mask_data)
print('{}  is ok !!!!!'.format(inpath))