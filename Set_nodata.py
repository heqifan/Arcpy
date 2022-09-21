
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *

def set_nodata(dir,outdir,scope,distinguish):
    arcpy.env.scratchWorkspace = dir
    env.workspace = dir
    List = arcpy.ListRasters(distinguish)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        print('{} is create ok!!!!!!'.format(outdir))
    for i in List:
        outSetNull = SetNull(i, i, scope)
        outSetNull.save(outdir  + os.sep + i)
        print(str(i) + ' Save is ok  !!!')



def set_nodata2(tif,outdir,scope):
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        print('{} is create ok!!!!!!'.format(outdir))
    outSetNull = SetNull(tif, tif, scope)
    outSetNull.save(outdir  + os.sep + tif)
    print(str(tif) + ' Save is ok  !!!')
styear = 2000
edyear = 2017

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

inpath = r'K:\HeQiFan\BMA'

outpath = r'E:\Integrated_analysis_data\Data\Out\BMA_Year'

scope =  "VALUE < 0"

distinguish = 'BMA*.tif'


arcpy.env.scratchWorkspace = inpath
env.workspace = inpath
List = arcpy.ListRasters(distinguish)
for tif in List:
    outdir = outpath + os.sep + str(styear)
    set_nodata2(tif,outdir,scope)
    styear += 1

# set_nodata(inpath,outpath,scope,distinguish)
