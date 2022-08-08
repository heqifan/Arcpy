
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


def SetNodata(indir,outdir,character):
    arcpy.env.scratchWorkspace = indir + os.sep
    env.workspace = indir + os.sep
    List = arcpy.ListRasters(character)
    if len(List) == 0:
        return 0
    for data in List:
        try:
            OutRas = Con(Raster(data)>=249,-1,data)
            OutRas.save(outdir + os.sep + "Con_" + data[:-4] + '.tif')
        except:
            print('{} is error continue'.format(data))
            continue
    return 1



path = {r'F:\Integrated_analysis_data\Data\LAI':'tif'}


styear = 2002
edyear = 2018

for inpath in path:
    print(inpath)
    character = 'Mask*.' + path[inpath]
    for year in range(styear, edyear + 1):
        indir = inpath + os.sep + 'MCD15A2_LAI_' + str(year)
        outdir = indir
        result = SetNodata(indir,outdir,character)
        print('-------Finish--------' if result==1 else '-------{}  is Empty--------'.format(indir))
        print('{} is ok '.format(year))
    print('{}  is ok !!!!!'.format(inpath))
