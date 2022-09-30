# coding:utf-8
import glob
import arcpy
from arcpy import env
import os
from arcpy.sa import *
import glob

arcpy.CheckOutExtension("Spatial")
arcpy.gp.overwriteOutput = 1

def M_to_points(year_list,inPointFeatures):
    ExtractMultiValuesToPoints(inPointFeatures, year_list, "BILINEAR")

styear = 2005
edyear = 2015



path = {
        r'E:\Integrated_analysis_data\Data\Vertify_out\Bagging_forest':'Bagging',}



inPointFeatures = r"E:\Integrated_analysis_data\Data\NPP_yz\npp_points_forest.shp"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute ExtractValuesToPoints

# print(name2)
for inpath in path:
    print(inpath)
    character = path[inpath] + '*.tif'
    name = path[inpath]
    year_list = []
    for year in range(styear, edyear + 1):
        tif = glob.glob(inpath + os.sep + str(year) + os.sep + character)[0]
        year_list.append([tif,name + '_' + str(year)])
    M_to_points(year_list, inPointFeatures)
# -- coding: utf-8 --
