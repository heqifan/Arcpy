# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
import pandas as pd

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

inpath = r'J:\Integrated_analysis_data\Data\1Y\GLASS_1982_2018_1y'
# inpath = r'K:\HeQiFan\0816\drive\out_temperature'
# dirs = ['Normal_LAI','Normal_Geodata','Normal_GLASS','Normal_MODIS','Normal_TPDC','Normal_W']
#
# distinguishs = ['Mask_*.tif','Mask_*.tif','Mask_*.tif','Mask_*.tif','Mask_*.tif','Mask_*.tif']

static_tif = r'J:\Integrated_analysis_data\Data\shp\QTPshp\Merge.shp'
# keys = [r'Mul_',r'Mul_',r'Resample_']
xlsx_path = r'E:\Wang_NPP_Region_Statical'
all_csv = []
styear = 1982
edyear = 2018
# for dir,dis in zip(dirs,distinguishs):
#     dir = inpath + os.sep + dir
#     arcpy.env.scratchWorkspace =  dir
#     env.workspace =  dir  #Setting up the workspace
#     List = arcpy.ListRasters(dis)
#     csv_list = []
#     for tif in List:
#         print(tif)
#         outTable = tif.split('.')[0] + '.dbf'
#         '''Zonal Statistics as Table'''
#         outZSaT = ZonalStatisticsAsTable(static_tif,'Value', tif,
#                                          outTable, "DATA", "MEAN")
#         '''Execute TableToTable'''
#         outcsv = tif.split('.')[0] + '.csv'
#         arcpy.TableToTable_conversion(outTable, dir, outcsv)
#
#         '''Statics'''
#         csv = list(pd.read_csv(dir + os.sep + outcsv).iloc[1:,:]['MEAN'])
#         csv_list.append(csv)
#     csv_list = [i for item in csv_list for i in item]   #Two dimensions to one dimension
#     all_csv.append(csv_list)
#
# '''Export Result'''
# all_csv = pd.DataFrame(all_csv).T
# all_csv.to_excel(xlsx_path + os.sep + 'bma.xlsx',index = False,header = None)

# for year in range(styear,edyear+1):
#     dir = inpath + os.sep + year +  '_Mean'
#     arcpy.env.scratchWorkspace =  dir
#     env.workspace =  dir  #Setting up the workspace
#     List = arcpy.ListRasters('*.tif')
#     csv_list = []
#     for tif in List:
#         print(tif)
#         outTable = tif.split('.')[0] + '.dbf'
#         '''Zonal Statistics as Table'''
#         outZSaT = ZonalStatisticsAsTable(static_tif,'Value', tif,
#                                          outTable, "DATA", "MEAN")
#         '''Execute TableToTable'''
#         outcsv = tif.split('.')[0] + '.csv'
#         arcpy.TableToTable_conversion(outTable, dir, outcsv)
#
#         '''Statics'''
#         csv = list(pd.read_csv(dir + os.sep + outcsv).iloc[1:,:]['MEAN'])
#         csv_list.append(csv)
#     csv_list = [i for item in csv_list for i in item]   #Two dimensions to one dimension
#     all_csv.append(csv_list)
#
# '''Export Result'''
# all_csv = pd.DataFrame(all_csv).T
# all_csv.to_excel(xlsx_path + os.sep + 'bma.xlsx',index = False,header = None)

all_pd = pd.DataFrame({'Regions':[1,2,3]})
for year in range(styear,edyear+1):
    dir = inpath + os.sep + str(year)
    # dir = inpath + os.sep + str(year) + '_Sum'
    arcpy.env.scratchWorkspace =  dir
    env.workspace =  dir  #Setting up the workspace
    tif = arcpy.ListRasters('Mul_*.tif')[0]
    print(tif)
    outTable = tif.split('.')[0] + '.dbf'
    '''Zonal Statistics as Table'''
    outZSaT = ZonalStatisticsAsTable(static_tif,'name', tif,
                                     outTable, "DATA", "MEAN")
    '''Execute TableToTable'''
    outcsv = tif.split('.')[0] + '.csv'
    arcpy.TableToTable_conversion(outTable, dir, outcsv)
    # pd.set_option('precision', 15)
    '''Statics'''
    # csv = pd.read_csv(dir + os.sep + outcsv).sort_values(["Value"],ascending=True)
    csv = pd.read_csv(dir + os.sep + outcsv)
    all_pd['Count'] = csv['COUNT']
    all_pd['MEAN' + str(year)] = csv['MEAN']
    # all_pd['Sum' + str(year)] = csv['MEAN']
'''Export Result'''
# all_pd.to_excel(xlsx_path + os.sep + 'Static_temperature.xlsx',index = False)
all_pd.to_excel(xlsx_path + os.sep + 'GLASS_mean.xlsx',index = False)