# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
import pandas as pd

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

# inpath = r'K:\HeQiFan\0816\drive\out_temperature'
inpath = r'K:\HeQiFan\0816\drive\out_precipitation'
# dirs = ['Normal_LAI','Normal_Geodata','Normal_GLASS','Normal_MODIS','Normal_TPDC','Normal_W']
#
# distinguishs = ['Mask_*.tif','Mask_*.tif','Mask_*.tif','Mask_*.tif','Mask_*.tif','Mask_*.tif']

static_tif = r'E:\Wang\Regions.tif'

xlsx_path = r'E:\Wang'
all_csv = []
styear = 2000
edyear = 2020
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

all_pd = pd.DataFrame({'Regions':[1,2,3,4]})
for year in range(styear,edyear+1):
    dir = inpath + os.sep + str(year) +  '_Mean'
    dir = inpath + os.sep + str(year) + '_Sum'
    arcpy.env.scratchWorkspace =  dir
    env.workspace =  dir  #Setting up the workspace
    tif = arcpy.ListRasters('*.tif')[0]
    outTable = tif.split('.')[0] + '.dbf'
    '''Zonal Statistics as Table'''
    outZSaT = ZonalStatisticsAsTable(static_tif,'Value', tif,
                                     outTable, "DATA", "MEAN")
    '''Execute TableToTable'''
    outcsv = tif.split('.')[0] + '.csv'
    arcpy.TableToTable_conversion(outTable, dir, outcsv)
    pd.set_option('precision', 15)
    '''Statics'''
    csv = pd.read_csv(dir + os.sep + outcsv).sort_values(["Value"],ascending=True)
    all_pd['Mean'+str(year)] = csv['MEAN']

'''Export Result'''
# all_pd.to_excel(xlsx_path + os.sep + 'Static_temperature.xlsx',index = False)
all_pd.to_excel(xlsx_path + os.sep + 'Static_precipitation.xlsx',index = False)