
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


# character = 'lai*.flt'
inpath = r'J:\Integrated_analysis_data\Data\8D\Geodata_1981_2018_8d' #输入路径
outpath = inpath + os.sep + 'to_1y_result'
# Press the green button in the gutter to run the script.

styear = 1981
edyear = 1999


character = 'NPP.*.tif'

def Mean(indir,outdir,character,Y_N,year):
    Sum = 0
    N = 0
    arcpy.env.scratchWorkspace =  indir + os.sep
    env.workspace =  indir + os.sep   #设置工作空间
    List = arcpy.ListRasters(character)
    if len(List) == 0:
        print('{} length is {}'.format(indir, len(List)))
        return 0
    for data in List[:-1]:
        print('Data: {} '.format(data))
        try:
            Sum += Raster(str(data)) * 8  # 相加
            N+=1
        except RuntimeError:
            print('{} is error continue'.format(data))
            continue
    if  Y_N == 'Y':
        Sum += Raster(str(List[-1])) * 6
    if  Y_N == 'N':
        Sum += Raster(str(List[-1])) * 5
    N += 1
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        print('{} is create ok!!!!!!'.format(outdir))
    (Sum/N).save(outdir + os.sep + 'Mean_' + str(year) + '.tif')
    print(outdir + ' is ok ')
    return 1



for year in range(styear,edyear+1):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):  # 判断是否是闰年
        print (u"{}是闰年".format(year))
        Y_N = 'Y'
    else:
        print(u'{}不是闰年'.format(year))
        Y_N = 'N'

    dir = inpath + os.sep + str(year)

    outdir = outpath + os.sep + str(year)
    Mean(dir,outdir,character,Y_N,year)
    print(outdir + ' is ok ')
print('ALL is ok !!!!!!!!!!!')
