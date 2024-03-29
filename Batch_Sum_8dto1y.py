# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1


# inpath = r'F:\Integrated_analysis_data\Data\LAI' #输入路径
# outpath = r'F:\Integrated_analysis_data\Data\1Y\LAI_2003_2017_1y'
# Press the green button in the gutter to run the script.

# styear = 2003
# edyear = 2017

# character = 'Con*.tif'
inpath = r'E:\Integrated_analysis_data\Data\8D\GLASS_1982_2018_8d' #输入路径
outpath = r'E:\Integrated_analysis_data\Data\1Y\GLASS_1982_2018_1y_chinese'
# Press the green button in the gutter to run the script.

styear = 2011
edyear = 2018


character = 'Mask_*.tif'

def Sum(indir,outdir,character,Y_N,year):
    Sum = 0
    arcpy.env.scratchWorkspace =  indir
    env.workspace =  indir   #设置工作空间
    List = arcpy.ListRasters(character)
    List.sort()
    print('List: {}'.format(List))
    if len(List) == 0:
        print('{} length is {}'.format(indir, len(List)))
        return 0
    for data in List[:-1]:
        print('Data: {} '.format(data))
        try:
            Sum += Raster(str(data)) * 8  # 相加
        except RuntimeError:
            print('{} is error continue'.format(data))
            continue
    if  Y_N == 'Y':
        Sum += Raster(str(List[-1])) * 6
        # print('Data: {} '.format(List[-1]))
    if  Y_N == 'N':
        Sum += Raster(str(List[-1])) * 5
        # print('Data: {} '.format(List[-1]))
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        print('{} is create ok!!!!!!'.format(outdir))
    (Sum).save(outdir + os.sep + 'Sum_' + str(year) + '.tif')
    return 1



for year in range(styear,edyear+1):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):  # 判断是否是闰年
        print (u"{}是闰年".format(year))
        Y_N = 'Y'
    else:
        print(u'{}不是闰年'.format(year))
        Y_N = 'N'
    dir  = inpath + os.sep +  str(year)
    outdir  = outpath + os.sep + str(year)
    Sum(dir,outdir,character,Y_N,year)
    print(outdir + ' is ok ')
print('ALL is ok !!!!!!!!!!!')

