
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/27 17:36
# @Author : Xihuang O.Y.

import numpy as np
import arcpy, os
from arcpy import sa
from arcpy.sa import *
from arcpy import env

arcpy.CheckOutExtension(r'Spatial')
arcpy.env.overwriteOutput = True


'''参数初始化'''
# 统计的各类种类Tif的路径
tifPath = [r'F:\MetoGrid\Data\PRCP/',
           r'F:\MetoGrid\Data\TAVG/',
           r'F:\MetoGrid\Data\SWRS']

# tifPath的文件命名识别关键字
keys = [r'PRCP_',r'TAVG_',r'SWRS_']

# 输入所用的------行政分区Shp
Region = [r'F:\MetoGrid\Data\Climate4region\CClimate4Regions.shp',
          r'F:\MetoGrid\Data\Climate4region\CClimate4Regions_Dissolve.shp']

# 对应的shp统计字段名称
joinID = [r'NAME', r'Id']

# 存放临时文件的路径
out_Path = r'F:\MetoGrid\out'

startY = 1980
endY = 2020+1

'''运行'''
for shpi in range(0, len(Region)):  #循环多个矢量
    pass
    for cla in range(0, len(tifPath)):   #循环每个文件夹
        env.workspace = tifPath[cla]   #设置工作空间
        tiffiles = arcpy.ListFiles(r'*' + keys[cla] + '*.tif')
        print('Process_Data have  :',tiffiles)
        #tiffiles.sort()   #将文件名进行排序（升序排序）
        tiffiles.sort()
        print(tiffiles)
        for filename,yr in zip(tiffiles,range(startY,endY)):
            ULC = env.workspace + os.sep + filename
            field = keys[cla].split(r'_')[0]  + r'_' + str(yr)    #定义字段名
            tempTable = out_Path + os.sep + field
            print(tempTable)
            # 关联字段 and 统计字段
            # 统计类型很有多种
            arcpy.gp.ZonalStatisticsAsTable(Region[shpi], joinID[shpi], ULC, tempTable, 'DATA', 'MEAN')   #分区统计：输出一张表
            # # 在shp文件中增加列的名称，根据需要选择字段类型
            arcpy.AddField_management(tempTable, field, 'DOUBLE')   #向表中添加字段
            arcpy.CalculateField_management(tempTable, field, '[MEAN]', 'VB', '')   #计算字段
            arcpy.JoinField_management(Region[shpi], joinID[shpi], tempTable, joinID[shpi], [field])   #空间连接


