
# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
import glob
arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


# path = {r'K:\HeQiFan\1Y\Geodata_2000_2017_1y':[r'K:\HeQiFan\1Y\Geodata_2000_2017_1y\Mean','Mask*.tif','Geodata'],
#         r'K:\HeQiFan\1Y\GLASS_2000_2017_1y':[r'K:\HeQiFan\1Y\GLASS_2000_2017_1y\Mean','Mask*.tif','GLASS'],
#         r'K:\HeQiFan\1Y\MODIS_2000_2017_1y':[r'K:\HeQiFan\1Y\MODIS_2000_2017_1y\Mean','Mask*.tif','MODIS'],
#         r'K:\HeQiFan\1Y\TPDC_2000_2017_1y':[r'K:\HeQiFan\1Y\TPDC_2000_2017_1y\Mean','Mask*.tif','TPDC'],
#         r'K:\HeQiFan\1Y\W_2000_2017_1y':[r'K:\HeQiFan\1Y\W_2000_2017_1y\Mean','Re*.tif','W'],
#         }


styear = 2000
edyear = 2020


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

def Mean2(year_list,outdir,name):
    Sum = 0
    N = 0
    if len(year_list) == 0:
        print('{} length is {}'.format(indir, len(year_list)))
        return 0
    for data in year_list:
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
    (Sum/N).save(outdir + os.sep + 'Mean_' + name + '.tif')
    print(outdir + ' is ok ')
    return 1

indir = r'K:\HeQiFan\0816\drive\out_precipitation'
# outdir = r'K:\HeQiFan\Out\Multiply_Regression_Year\Mean'

character = '*.tif'

# Mean(indir, outdir,character)

for year in range(styear,edyear+1):
    dir  = indir + os.sep + str(year)
    outdir  = dir + os.sep + 'Mean'
    Mean(dir,outdir,character)
    print(outdir + ' is ok ')
print('ALL is ok !!!!!!!!!!!')


# for pa in path:
#     year_list = []
#     character = path[pa][1]
#     for year in range(styear, edyear+1):
#         indir = pa  + os.sep + str(year)
#         tif = glob.glob(indir + os.sep + character)[0]
#         year_list.append(tif)
#     outdir = path[pa][0]
#     NAME = path[pa][2]
#     Mean2(year_list,outdir,NAME)
#     print(indir + ' is ok ')
# print('ALL is ok !!!!!!!!!!!')

