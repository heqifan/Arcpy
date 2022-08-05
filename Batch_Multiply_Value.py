# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


<<<<<<< HEAD
inpath = r'F:\Integrated_analysis_data\Data\1Y\LAI_2003_2017_1y' #输入路径
outpath = r'F:\Integrated_analysis_data\Data\1Y\LAI_2003_2017_1y'
# Press the green button in the gutter to run the script.

styear = 2003
edyear = 2017


Multiply_Value = 0.1

character = 'Sum_*.tif'
=======
inpath = r'F:\Integrated_analysis_data\Data\1Y\TPDC_2000_2017_1y' #输入路径
outpath = r'F:\Integrated_analysis_data\Data\1Y\TPDC_2000_2017_1y'
# Press the green button in the gutter to run the script.

styear = 2000
edyear = 2017


Multiply_Value = 0.01

character = 'Resample_*.tif'
>>>>>>> d35dc003b7a04dbdf7a7ceb6aa1440e542219b3a

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
        Mul.save(outdir + os.sep + 'Mul_' + str(year) + '.tif')
    return 1



for year in range(styear,edyear+1):
    dir  = inpath + os.sep + str(year)
    outdir  = outpath + os.sep + str(year)
    Sum(dir,outdir,character,Multiply_Value,year)
    print(outdir + ' is ok ')
print('ALL is ok !!!!!!!!!!!')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
