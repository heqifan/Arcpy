<<<<<<< HEAD
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


inpath = r'F:\sum_1110\RNEP' #输入路径
outpath = r'E:\陈星师姐\2\NEP_10y_Mean'
# Press the green button in the gutter to run the script.

styear = 2000
edyear = 2018

character = 'NPP_*.tif'

def Mean(indir,outdir,character):
    Sum = 0
    N = 0
    arcpy.env.scratchWorkspace =  indir + os.sep
    env.workspace =  indir + os.sep   #设置工作空间
    List = arcpy.ListRasters(character)
    if len(List) == 0:
        print('{} length is {}'.format(indir, len(List)))
        return 0
    for data in List:
        print('Data: {} '.format(data))
        try:
            Sum += Raster(str(data))  # 相加
            N+=1
        except RuntimeError:
            print('{} is error continue'.format(data))
            continue
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        print('{} is create ok!!!!!!'.format(outdir))
    (Sum/N).save(outdir + os.sep + 'Mean_' + indir + '.tif')
    print(outdir + ' is ok ')
    return 1



for year in range(styear,edyear+1):
    dir  = inpath + os.sep + str(year)
    outdir  = outpath + os.sep + str(year)
    Mean(dir,outdir,character)
    print(outdir + ' is ok ')
print('ALL is ok !!!!!!!!!!!')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
=======
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


inpath = r'F:\sum_1110\RNEP' #输入路径
outpath = r'E:\陈星师姐\2\NEP_10y_Mean'
# Press the green button in the gutter to run the script.

styear = 2000
edyear = 2018

character = 'NPP_*.tif'

def Mean(indir,outdir,character):
    Sum = 0
    N = 0
    arcpy.env.scratchWorkspace =  indir + os.sep
    env.workspace =  indir + os.sep   #设置工作空间
    List = arcpy.ListRasters(character)
    if len(List) == 0:
        print('{} length is {}'.format(indir, len(List)))
        return 0
    for data in List:
        print('Data: {} '.format(data))
        try:
            Sum += Raster(str(data))  # 相加
            N+=1
        except RuntimeError:
            print('{} is error continue'.format(data))
            continue
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        print('{} is create ok!!!!!!'.format(outdir))
    (Sum/N).save(outdir + os.sep + 'Mean_' + indir + '.tif')
    print(outdir + ' is ok ')
    return 1



for year in range(styear,edyear+1):
    dir  = inpath + os.sep + str(year)
    outdir  = outpath + os.sep + str(year)
    Mean(dir,outdir,character)
    print(outdir + ' is ok ')
print('ALL is ok !!!!!!!!!!!')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
>>>>>>> 50a0148 (first commit)
