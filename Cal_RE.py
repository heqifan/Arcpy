<<<<<<< HEAD
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

inpath = r'F:\Wu\Data\T'
env.workspace = inpath + os.sep
arcpy.env.scratchWorkspace = inpath + os.sep

for year in range(2003,2010+1):
    gpp = inpath + os.sep + 'RGPP_' + str(year) + '.flt'
    npp = inpath + os.sep + 'RNPP_' + str(year) + '.flt'
    re  = Raster(str(gpp)) - Raster(str(npp))
    (re).save('F:\\Wu\\Data\\T\\' + 'RE_' + str(year) + '.tif')
=======
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

inpath = r'F:\Wu\Data\T'
env.workspace = inpath + os.sep
arcpy.env.scratchWorkspace = inpath + os.sep

for year in range(2003,2010+1):
    gpp = inpath + os.sep + 'RGPP_' + str(year) + '.flt'
    npp = inpath + os.sep + 'RNPP_' + str(year) + '.flt'
    re  = Raster(str(gpp)) - Raster(str(npp))
    (re).save('F:\\Wu\\Data\\T\\' + 'RE_' + str(year) + '.tif')
>>>>>>> 50a0148 (first commit)
    print(str(year) + ' is ok !!!!!!!!')