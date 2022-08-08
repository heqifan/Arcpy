
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


def mask(indir,outdir,mask_data,character,prj_path,reproject_type):
    arcpy.env.scratchWorkspace = indir + os.sep
    env.workspace = indir + os.sep
    List = arcpy.ListRasters(character)
    if len(List) == 0:
        return 0
    for data in List:
        try:
            arcpy.ProjectRaster_management(data, outdir + os.sep + "Reproject_" + data ,prj_path,reproject_type)
            outExtractByMask = ExtractByMask(outdir + os.sep + "Reproject_" + data, mask_data)
            outExtractByMask.save(outdir + os.sep + 'Mask_' + data)
        except:
            print('{} is error continue'.format(data))
            continue
    return 1

path = {r'F:\Integrated_analysis_data\Data\Geodata_1981_2018_8d':'tif',r'F:\Integrated_analysis_data\Data\GLASS_1982_2018_8d':'tif',
        r'F:\Integrated_analysis_data\Data\MODIS_2000_2020_1y':'tif',r'F:\Integrated_analysis_data\Data\TPDC_2000_2017_1y':'tif'}


mask_data = r'F:\Integrated_analysis_data\Data\mask\2000_npp.tif'

prj_path  = r'F:\Integrated_analysis_data\Data\prj\RNPP_2018.prj'

reproject_type = 'CUBIC'

styear = 2000
edyear = 2017

for inpath in path:
    print(inpath)
    character = 'Mask_*.' + path[inpath]
    for year  in range(styear,edyear+1):
        indir = inpath + os.sep + str(year)
        outdir = indir
        mask(indir,outdir,mask_data,character,prj_path)
        print('{} is ok '.format(year))
    print('{}  is ok !!!!!'.format(inpath))
