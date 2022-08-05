# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *

def set_nodata(datatype,outdir,scope):
    List = arcpy.ListRasters('*.' + datatype)
    for i in List:
        outSetNull = SetNull(i, i, scope)
        outSetNull.save(outdir  + os.sep + i)
        print(str(i) + ' Save is ok  !!!')

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

inpath = r'F:\MetoGrid\Annual_'
datatype = 'tif'
arcpy.env.scratchWorkspace = inpath + os.sep
env.workspace = inpath + os.sep
outdir = inpath
scope =  "VALUE < -9000"

set_nodata(datatype,outdir,scope)