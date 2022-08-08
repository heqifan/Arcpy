
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

def Resample(indir,outdir,cellsize, character,resample_type):
    arcpy.env.scratchWorkspace = indir + os.sep
    env.workspace = indir + os.sep
    List = arcpy.ListRasters(character)
    if len(List) == 0:
        return 0
    for data in List:
        try:
            arcpy.Resample_management(data, outdir + os.sep + 'Resample_' + data , cellsize, resample_type)
        except:
            print('{} is error continue'.format(data))
            continue
    return 1


#
# path = {r'F:\Integrated_analysis_data\Data\Geodata_1981_2018_8d':'tif',r'F:\Integrated_analysis_data\Data\GLASS_1982_2018_8d':'tif',
#         r'F:\Integrated_analysis_data\Data\MODIS_2000_2020_1y':'tif',r'F:\Integrated_analysis_data\Data\TPDC_2000_2017_1y':'tif'}
#path = {r'F:\Integrated_analysis_data\Data\TPDC_2000_2017_1y':'tif'}

path = {r'F:\Integrated_analysis_data\Data\1Y\TPDC_2000_2017_1y':'tif'}


example_data = r'F:\Integrated_analysis_data\Data\Resample\RNPP_2016_reproject.tif'

cellsize = "{0} {1}".format(arcpy.Describe(example_data).meanCellWidth,arcpy.Describe(example_data).meanCellHeight)
print('Cellsize:',cellsize)

styear = 2000
edyear = 2017

resample_type = 'CUBIC'

for inpath in list(path.keys()):
    print(inpath)

    character = 'Mask_*' + path[inpath]
    for year in range(styear, edyear + 1):
        indir = inpath + os.sep + str(year)
        outdir = indir
        result = Resample(indir,outdir,cellsize, character,resample_type)
        print('-------{} is Finish--------'.format(indir) if result==1 else '-------{}  is Empty--------'.format(indir))
    print('{}  is ok !!!!!'.format(inpath))
print('All is ok !!!!!!')