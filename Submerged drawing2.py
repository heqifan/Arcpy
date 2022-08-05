# coding:utf-8
import glob
import arcpy
import os
from arcpy.sa import *

arcpy.CheckOutExtension("spatial")
arcpy.gp.overwriteOutput = 1
arcpy.env.parallelProcessingFactor = "0"


'''下面的路径都与model_new1.py里面的相同，意思就是model_new1.py里面的路径是啥，下面的就是啥'''

# 最后存放的文件夹路径
result_path = r'D:\xiangmushuju\result'

# 工作空间（放中间数据）
tem_path = r'D:\xiangmushuju\linshi'

# 横断面数据存放的文件夹
shp_path = r'D:\xiangmushuju\heliuduanmian\drop'


def start_(str1):
    print("Processing: " + str1 + '\t')

def end_(str2):
    print(str2 + '\t' + 'is ok------' + '\t')

def Process2(result_dir, name, work_space,tf):

    arcpy.env.workspace = work_space
    GISfile = result_dir + os.sep + 'GISfile'
    Output_raster = name + '_' + "Output_raster.tif"
    Output_flow_direction_raster = name + '_' + "Output_flow_direction_raster.tif"
    Output_polygon_features = name + '_'+ "Output_polygon_features.shp"
    if tf:
        '''如果需要重新处理同一数据时，请将下面代码注释 如果希望跳过已经处理好数据，请取消注释'''
        if  len(glob.glob(GISfile + os.sep + '*.shp'))==3:
            print('The data already exists.........Automatic exit      !!!!!!!')
            return
        print('\n')
        print('This data is output for the first time......go  on  !!!!!!!')
        print('\n')

    outFeatureClass = GISfile + os.sep + name + "子流域.shp"
    incline = GISfile + os.sep + name + "断面.shp"

    start_('Add Field')  # 添加字段
    arcpy.AddField_management(incline, "Name2", "TEXT")
    end_('Add Field')

    start_('Calculate Field')  # 计算字段
    arcpy.CalculateField_management(incline, "Name2", "!Name![2:]", "PYTHON_9.3")
    end_('Calculate Field')

    start_('Add Field')  # 添加字段
    arcpy.AddField_management(incline, "gridcode", "DOUBLE")
    end_('Add Field')

    start_('Calculate Field')  # 计算字段
    arcpy.CalculateField_management(incline, "gridcode", "Int ( [Name2] )-1", "VB")
    end_('Calculate Field')

    # start_('Add Field')  # 添加字段
    # arcpy.AddField_management(incline, "gridcode", "DOUBLE")
    # end_('Add Field')
    #
    # start_('Calculate Field')  # 计算字段
    # arcpy.CalculateField_management(incline, "gridcode", "[Name3]", "VB")
    # end_('Calculate Field')
    #
    start_('Snap Pour Point')  # 捕捉
    Output_raster__2_ = SnapPourPoint(incline, Output_raster, 0, "gridcode")
    Output_raster__2_.save(arcpy.env.workspace + os.sep + name + '_' + "Output_raster__2_.tif")
    end_('Snap Pour Point')

    start_('Watershed')  # 生成流域栅格数据
    Output_raster__3_ = Watershed(Output_flow_direction_raster, Output_raster__2_, "VALUE")
    Output_raster__3_.save(arcpy.env.workspace + os.sep + name + '_' + "Output_raster__3_.tif")
    end_('Watershed')

    start_('Raster to Polygon')  # 将流域栅格数据转为矢量
    arcpy.RasterToPolygon_conversion(Output_raster__3_, Output_polygon_features, "SIMPLIFY", "VALUE")
    end_('Raster to Polygon')

    start_('Dissolve')  # 融合
    arcpy.Dissolve_management(Output_polygon_features, outFeatureClass, "gridcode")
    end_('Dissolve')

    start_('Add Field')  # 添加字段
    arcpy.AddField_management(outFeatureClass, "area", "DOUBLE")
    end_('Add Field')

    start_('Calculate Field')  # 计算字段
    arcpy.CalculateField_management(outFeatureClass, "area", "!shape.area!*0.000001", "PYTHON_9.3")
    end_('Calculate Field')

    start_('Intersect')  # 连接字段
    arcpy.JoinField_management(incline, 'gridcode', outFeatureClass, 'gridcode')
    end_('Intersect')

    start_('Calculate Length')  # 计算长度
    arcpy.AddGeometryAttributes_management(incline, "LENGTH_GEODESIC", "METERS")
    end_('Calculate Length')

def main_(result_path, tem_path,shp_path,tf):
    """
        Args:
            result_path: 结果文件夹
            tem_path：工作空间（临时文件夹）
            shp_path: kml数据文件夹
            tf: 是否要跳过相同数据的输出  True为跳过，False为不跳过
        Returns:
    """
    tem_dir = tem_path + os.sep + 'tempory'
    lines = glob.glob(shp_path + os.sep + '*.shp')
    if not os.path.exists(tem_dir):
        os.makedirs(tem_dir)
        print('Tem_dir \tis create ok!!!!!!!!!\t', tem_dir)
    for line in lines:
        print('Processing:\t', line)
        name = line.split('\\')[-1].split('.')[0]
        every_dir = result_path + os.sep + name
        if not os.path.exists(every_dir):
            os.makedirs(every_dir)
        Process2(every_dir, name,tem_dir,tf)
        print ('Processed:\t', line)
        print "---------------------successful!!!!!!!!!!!!!!!-----------------------"

    print('---------------------------------all is ok----------------------------------------')

main_(result_path, tem_path,shp_path,True)