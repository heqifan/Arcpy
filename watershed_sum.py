# -- coding: utf-8 --

import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

#
# inpath = r'F:\sum_1110\RNEP' #输入路径
# outpath = r'E:\陈星师姐\2\NEP_10y_Mean'
# # Press the green button in the gutter to run the script.
#
# styear = 2000
# edyear = 2018
#
# character = 'NPP_*.tif'
#
# def Sum(indir,outdir,character):
#     Sum = 0
#     arcpy.env.scratchWorkspace =  indir + os.sep
#     env.workspace =  indir + os.sep   #设置工作空间
#     List = arcpy.ListRasters(character)
#     if len(List) == 0:
#         print('{} length is {}'.format(indir, len(List)))
#         return 0
#     for data in List:
#         print('Data: {} '.format(data))
#         try:
#             Sum += Raster(str(data))  # 相加
#         except RuntimeError:
#             print('{} is error continue'.format(data))
#             continue
#     if not os.path.exists(outdir):
#         os.makedirs(outdir)
#         print('{} is create ok!!!!!!'.format(outdir))
#     (Sum).save(outdir + os.sep + 'Sum_' + indir + '.tif')
#     print(outdir + ' is ok ')
#     return 1
#
#
#
# for year in range(styear,edyear+1):
#     dir  = inpath + os.sep + str(year)
#     outdir  = outpath + os.sep + str(year)
#     Sum(dir,outdir,character)
#     print(outdir + ' is ok ')
# print('ALL is ok !!!!!!!!!!!')
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#


vars =  ['evabs','evaow','evatc','evavt','pev','e','tp']
styear = 1950
edyear = 2021
inpath = r'J:\out_netcdf'
outpath = r'J:\out_netcdf\out'
for var in vars:
    # print(var)
    outdir  = outpath + os.sep + var
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        # print('{} is create ok!!!!!!'.format(outdir))
    for year in range(styear,edyear+1):
        # print(year)
        n = 0
        Sum = 0
        for num_month in range(1,12+1):
            str_month = "%02d"%num_month
            # print(str_month)
            if num_month>=10:
                data = inpath + os.sep + "ERA5_China." + str(year) + '_' + \
                    str_month + os.sep + "ERA5_China." + str(year) + '_1_' + var + '_0.tif'
            else:
                data = inpath + os.sep + "ERA5_China." + str(year) + '_' + \
                    str_month + os.sep + "ERA5_China." + str(year) + '_0_' + var + '_0.tif'
            # print(data)
            n+=1
            Sum += Raster(data)  # 相加
        (Sum).save(outdir + os.sep + 'Sum_' + str(year) + '_' + var + '.tif')
        print(str(year) + 'is ok!!!!')
        print('{} 的月份总数量为{}'.format(year,n))
    print(var + 'is ok')
print('all is ok !!!!!!')
