
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
    for i in List:
        outSetNull = SetNull(i, i, scope)
        outSetNull.save(outdir  + os.sep + i)
        print(str(i) + ' Save is ok  !!!')


styear = 2000
edyear = 2017

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

inpath = r'K:\HeQiFan\1Y\MODIS_2000_2017_1y'

outpath = r'K:\HeQiFan\1Y\MODIS_2000_2017_1y'

scope =  "VALUE < 0"

distinguish = 'Mask*.tif'


for year in range(styear,edyear+1):
    dir  = inpath + os.sep + str(year)
    outdir  = outpath + os.sep + str(year)
    set_nodata(dir,outdir,scope,distinguish)
    print(outdir + ' is ok ')
print('ALL is ok !!!!!!!!!!!')

# set_nodata(inpath,outpath,scope,distinguish)