
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


def Mask(indir,outdir,mask_data,character):
    arcpy.env.scratchWorkspace = indir
    env.workspace = indir
    arcpy.env.snapRaster = mask_data  # snap栅格
    arcpy.env.extent = mask_data  # 像元行列号一致
    List = arcpy.ListRasters(character)
    if len(List) == 0:
        return 0
    for data in List:
        try:
            outExtractByMask = ExtractByMask(data, mask_data)
            outExtractByMask.save(outdir + os.sep + "Mask_" + data[:-4] + '.tif')
        except:
            print('{} is error continue'.format(data))
            continue
    return 1

# path = {r'K:\HeQiFan\Out\Normal_Geodata':'Nor*.tif',r'K:\HeQiFan\Out\Normal_GLASS':'Nor*.tif',r'K:\HeQiFan\Out\Normal_MODIS':'Nor*.tif',
#         r'K:\HeQiFan\Out\Normal_TPDC':'Nor*.tif',r'K:\HeQiFan\Out\Normal_W':'Nor*.tif',r'K:\HeQiFan\Out\Normal_LAI':'Nor*.tif'}
# path = {r'K:\HeQiFan\Out\Normal_Geodata':'Nor*.tif'}
#
# mask_data = r'K:\HeQiFan\Sample\Mask_Mul_2009.tif'
#
#
styear = 1981
edyear = 2018


# for inpath in path:
#     print(inpath)
#     character = path[inpath]
#     result = Mask(inpath,inpath,mask_data,character)
#     print('-------Finish--------' if result==1 else '-------{}  is Empty--------'.format(inpath))
#     print('{}  is ok !!!!!'.format(inpath))


# for inpath in path:
#     print(inpath)
#     character = 'Reproject_*.' + path[inpath]
#     for year in range(styear, edyear + 1):
#         indir = inpath + os.sep + str(year)
#         outdir = indir
#         result = Mask(indir,outdir,mask_data,character)
#         print('-------Finish--------' if result==1 else '-------{}  is Empty--------'.format(indir))
#         print('{} is ok '.format(year))
#     print('{}  is ok !!!!!'.format(inpath))

inpath = r'E:\Integrated_analysis_data\Data\1Y\MuSyQ_1981_2018_1y_chinese'

sample_tif = r'E:\Integrated_analysis_data\Data\chinese_mask\Mean_GLOPEM-CEVSA.tif'

# dirs = os.listdir(inpath)
# for file in dirs:
#     dirpath = inpath + os.sep +  file
#     result = Mask(dirpath,dirpath,sample_tif,'*.tif')
#     print('-------Finish--------' if result==1 else '-------{}  is Empty--------'.format(dirpath))
#     print('{} is ok '.format(file))

character = 'Resample*.tif'
for year in range(styear, edyear + 1):
    indir = inpath + os.sep + str(year)
    outdir = inpath + os.sep + str(year)
    result = Mask(indir,outdir,sample_tif,character)
    print('-------Finish--------' if result==1 else '-------{}  is Empty--------'.format(indir))
    print('{} is ok '.format(year))
print('{}  is ok !!!!!'.format(inpath))