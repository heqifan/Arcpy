# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
import pandas as pd

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

inpath = r'K:\HeQiFan\Out'

dirs = ['Normal_LAI','Normal_Geodata','Normal_GLASS','Normal_MODIS','Normal_TPDC','Normal_W']

distinguishs = ['Mask_*.tif','Mask_*.tif','Mask_*.tif','Mask_*.tif','Mask_*.tif','Mask_*.tif']

static_tif = r'K:\HeQiFan\Grass\CGrassChina_mask.tif'

csv_path = r'K:\HeQiFan\BMA'
all_csv = []
for dir,dis in zip(dirs,distinguishs):
    dir = inpath + os.sep + dir
    arcpy.env.scratchWorkspace =  dir
    env.workspace =  dir  #Setting up the workspace
    List = arcpy.ListRasters(dis)
    csv_list = []
    for tif in List:
        print(tif)
        outTable = tif.split('.')[0] + '.dbf'
        '''Zonal Statistics as Table'''
        outZSaT = ZonalStatisticsAsTable(static_tif,'Value', tif,
                                         outTable, "DATA", "MEAN")
        '''Execute TableToTable'''
        outcsv = tif.split('.')[0] + '.csv'
        arcpy.TableToTable_conversion(outTable, dir, outcsv)

        '''Statics'''
        csv = list(pd.read_csv(dir + os.sep + outcsv).iloc[1:,:]['MEAN'])
        csv_list.append(csv)
    csv_list = [i for item in csv_list for i in item]   #Two dimensions to one dimension
    all_csv.append(csv_list)

'''Export Result'''
all_csv = pd.DataFrame(all_csv).T
all_csv.to_excel(csv_path + os.sep + 'bma.xlsx',index = False,header = None)
