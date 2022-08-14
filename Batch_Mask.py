
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


def Mask(indir,outdir,mask_data,character):
    arcpy.env.scratchWorkspace = indir + os.sep
    env.workspace = indir + os.sep
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
path = {r'K:\HeQiFan\Out\Normal_Geodata':'Nor*.tif'}

mask_data = r'K:\HeQiFan\Sample\Mask_Mul_2009.tif'


styear = 2003
edyear = 2017

for inpath in path:
    print(inpath)
    character = 'Reproject_*.' + path[inpath]
    for year in range(styear, edyear + 1):
        indir = inpath + os.sep + str(year)
        outdir = indir
        result = Mask(indir,outdir,mask_data,character)
        print('-------Finish--------' if result==1 else '-------{}  is Empty--------'.format(indir))
        print('{} is ok '.format(year))
    print('{}  is ok !!!!!'.format(inpath))
# for inpath in path:
#     print(inpath)
#     character = path[inpath]
#     result = Mask(inpath,inpath,mask_data,character)
#     print('-------Finish--------' if result==1 else '-------{}  is Empty--------'.format(inpath))
#     print('{}  is ok !!!!!'.format(inpath))