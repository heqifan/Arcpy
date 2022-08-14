
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


inpath = r'K:\HeQiFan\Out\Normal_Mean_Year' #输入路径
outpath = r'K:\HeQiFan\Out\Normal_Mean_Year\Mean'
# Press the green button in the gutter to run the script.

styear = 2000
edyear = 2018

character = 'Nor*.tif'

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
    (Sum/N).save(outdir + os.sep + 'Mean_' + indir.split('\\')[-1] + '.tif')
    print(outdir + ' is ok ')
    return 1



# for year in range(styear,edyear+1):
#     dir  = inpath + os.sep + str(year)
#     outdir  = outpath + os.sep + str(year)
#     Mean(dir,outdir,character)
#     print(outdir + ' is ok ')
# print('ALL is ok !!!!!!!!!!!')
Mean(inpath,outpath,character)
print(outpath + ' is ok ')
print('ALL is ok !!!!!!!!!!!')

