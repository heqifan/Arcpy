
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
    List = arcpy.ListRasters(character)
    if len(List) == 0:
        return 0
    for data in List:
        try:
            outExtractByMask = ExtractByMask(data, mask_data)

            outExtractByMask.save(outdir + os.sep + "Mask_" + data[:-4] + '.tif')

            outExtractByMask.save(outdir + os.sep + "Mask_" + data)

        except:
            print('{} is error continue'.format(data))
            continue
    return 1




path = {r'F:\Integrated_analysis_data\Data\LAI':'flt'}

mask_data = r'F:\Integrated_analysis_data\Data\mask\Mul_2000.tif'

styear = 2002
edyear = 2018

for inpath in path:
    print(inpath)
    character = 'lai*.' + path[inpath]
    for year in range(styear, edyear + 1):
        indir = inpath + os.sep + 'MCD15A2_LAI_' + str(year)

path = {r'F:\Integrated_analysis_data\Data\Geodata_1981_2018_8d':'tif',r'F:\Integrated_analysis_data\Data\GLASS_1982_2018_8d':'tif',
        r'F:\Integrated_analysis_data\Data\MODIS_2000_2020_1y':'tif',r'F:\Integrated_analysis_data\Data\TPDC_2000_2017_1y':'tif'}

mask_data = r'F:\Integrated_analysis_data\Data\mask\2000_npp.tif'

styear = 2000
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
