
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1



# inpath = r'F:\Integrated_analysis_data\Data\1Y\LAI_2003_2017_1y' #输入路径
# outpath = r'F:\Integrated_analysis_data\Data\1Y\LAI_2003_2017_1y'
# Press the green button in the gutter to run the script.

styear = 1982
edyear = 1999


Multiply_Value = 1

character = 'Mask_*.tif'

inpath = r'J:\Integrated_analysis_data\Data\1Y\W_1982_2018_1y' #输入路径
outpath = r'J:\Integrated_analysis_data\Data\1Y\W_1982_2018_1y'
# Press the green button in the gutter to run the script.


def Sum(indir,outdir,character,Multiply_Value,year):
    arcpy.env.scratchWorkspace =  indir + os.sep
    env.workspace =  indir + os.sep   #设置工作空间
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        print('{} is create ok!!!!!!'.format(outdir))
    List = arcpy.ListRasters(character)
    if len(List) == 0:
        print('{} length is {}'.format(indir, len(List)))
        return 0
    for data in List:
        Mul = 0
        print('Data: {} '.format(data))
        try:
            Mul = Raster(str(data))*Multiply_Value  # 相加
        except RuntimeError:
            print('{} is error continue'.format(data))
            continue
        Mul.save(outdir + os.sep + 'Resample_' + str(year) + '.tif')
    return 1


for year in range(styear,edyear+1):
    dir = inpath + os.sep + str(year)
    outdir = outpath + os.sep + str(year)
    Sum(dir,outdir,character,Multiply_Value,year)
    print(outdir + ' is ok ')
print('ALL is ok !!!!!!!!!!!')
