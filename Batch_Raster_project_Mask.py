
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
        # try:
        out_name = outdir + os.sep + "Mask_" + data[:-4] + '.tif'
        # (fname, fename) = os.path.splittext(out_name)
        if (os.path.exists(out_name)):
            print('exist,continue')
            continue
        else:
            print(data)
            arcpy.ProjectRaster_management(data, outdir + os.sep + "Reproject_" + data[:-4] + ".tif", prj_path, reproject_type,'1000')
            # arcpy.env.snapRaster = mask_data  # snap栅格
            # arcpy.env.extent = mask_data  # 像元行列号一致
            outExtractByMask = ExtractByMask(outdir + os.sep + "Reproject_" + data[:-4] + ".tif", mask_data)
            outExtractByMask.save(out_name)
            print(out_name)
        # except:
        #     # print(arcpy.GetMessages(2))
        #     print('{} is error continue'.format(data))
        #     continue
    return 1

# path = {r'F:\Integrated_analysis_data\Data\1Y\LAI_2003_2017_1y':'tif'}
prj_path  = r'E:\Integrated_analysis_data\Data\prj\WGS_1984_Albers.prj'

reproject_type = 'BILINEAR'

mask_data = r'E:\Integrated_analysis_data\Data\Chinese_Regeion\chinese.shp'

inpath = r'E:\Integrated_analysis_data\Data\1Y\MODIS_2000_2017_1y_chinese'


styear = 2017
edyear = 2017

character = 'mosaic*.tif'
for year  in range(styear,edyear+1):
    indir = inpath + os.sep + str(year)
    outdir = inpath + os.sep + str(year)
    Raster_Project(indir,outdir,character,prj_path,reproject_type,mask_data)
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