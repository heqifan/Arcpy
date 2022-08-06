<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:20:39 2021
@author: Administrator
"""

import os
import arcpy
from arcpy import env
from arcpy.sa import *

def mosaic(outdir,datatype):
    rasters = arcpy.ListRasters("*." + datatype)
    rasters2 = []
    for ras in rasters:
        rasters2.append(ras)
    ras_list2 = ";".join(rasters2)
    print(ras_list2)
    try:
        arcpy.MosaicToNewRaster_management(ras_list2, outdir, "mosaic.tif", "", "16_BIT_SIGNED", "", "1", "", "")
        print('finish')
    except:
        print('error continue')
        return 0
    return 1



arcpy.CheckOutExtension("Spatial")
inpath = r'F:\GPP\MODIS'
dirs = os.listdir(inpath)
datatype = 'hdf'
for dir in dirs:
    print(dir)
    arcpy.env.scratchWorkspace = inpath + os.sep + dir
    env.workspace = inpath + os.sep + dir
    outdir = inpath + os.sep + dir
    mosaic(outdir,datatype)
    print('{} is ok '.format(dir))
=======
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:20:39 2021
@author: Administrator
"""

import os
import arcpy
from arcpy import env
from arcpy.sa import *

def mosaic(outdir,datatype):
    rasters = arcpy.ListRasters("*." + datatype)
    rasters2 = []
    for ras in rasters:
        rasters2.append(ras)
    ras_list2 = ";".join(rasters2)
    print(ras_list2)
    try:
        arcpy.MosaicToNewRaster_management(ras_list2, outdir, "mosaic.tif", "", "16_BIT_SIGNED", "", "1", "", "")
        print('finish')
    except:
        print('error continue')
        return 0
    return 1



arcpy.CheckOutExtension("Spatial")
inpath = r'F:\GPP\MODIS'
dirs = os.listdir(inpath)
datatype = 'hdf'
for dir in dirs:
    print(dir)
    arcpy.env.scratchWorkspace = inpath + os.sep + dir
    env.workspace = inpath + os.sep + dir
    outdir = inpath + os.sep + dir
    mosaic(outdir,datatype)
    print('{} is ok '.format(dir))
>>>>>>> 50a0148 (first commit)
print('ALL is finish!!!!!')