
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
        print(data)
        OutRas = Con(IsNull(Raster(data)),0,Raster(data))
        OutRas.save(outdir + os.sep + 'Con_' + data)
    return 1



path = {
        r'E:\Integrated_analysis_data\Data\Vertify_out\Bagging_forest':'Bagging*.tif'}


styear = 2000
edyear = 2017

for inpath in path:
    print(inpath)
    character = path[inpath]
    for year in range(styear, edyear + 1):
        indir = inpath + os.sep + str(year)
        outdir = indir
        result = SetNodata(indir,outdir,character)
        print('-------Finish--------' if result==1 else '-------{}  is Empty--------'.format(indir))
        print('{} is ok '.format(year))
    print('{}  is ok !!!!!'.format(inpath))
