# coding:utf-8
import glob
import arcpy
import os
from arcpy.sa import *

arcpy.CheckOutExtension("spatial")
arcpy.gp.overwriteOutput = 1
arcpy.env.parallelProcessingFactor = "0"


'''需要修改的地方'''
# 最后存放数据的文件夹路径（最终数据就在这里找哦）
result_path = r'D:\xiangmushuju\result'

# 工作空间（放中间数据）的路径
tem_path = r'D:\xiangmushuju\linshi'

# dem数据存放的文件夹路径（格式：tif）
dem_path = r'D:\xiangmushuju\dem2\dem'

# 横断面数据存放的文件夹 （格式：shp)
shp_path = r'D:\xiangmushuju\heliuduanmian\drop'

'''以下代码不需要修改'''
def start_(str1):
    print("Processing: " + str1 + '\t')


def end_(str2):
    print(str2 + '\t' + 'is ok------' + '\t')


def Process1(fill_dem, shp, work_space, result_path,name,tf):

    """
        Args:
            fill_dem: dem数据的绝对路径
            shp: 横断面数据的绝对路径
            work_space: 工作空间（临时文件夹）
            result_path: “成果”文件夹路径
            name: 数据名
            tf:是否重复输出相同数据   True为跳过，False为不跳过
        Returns:
    """

    every_dir = result_path + os.sep + name

    if tf:
        '''如果需要重新处理同一数据时，请将下面代码注释 如果希望跳过已经处理好数据，请取消注释'''
        if os.path.exists(every_dir):
            print('The data already exists.........Automatic exit      !!!!!!!')
            return
        print('\n')
        print('This data is output for the first time......go  on  !!!!!!!')
        print('\n')

    if os.path.exists(every_dir):
        os.makedirs(every_dir)

    arcpy.env.workspace = work_space
    Output_surface_raster = name + '_' + "Output_surface_raster.tif"
    Output_accumulation_raster = name + '_' + "Output_accumulation_raster.tif"
    Output_flow_direction_raster = name + '_' + 'Output_flow_direction_raster.tif'
    #incline = name + '_' + 'incline.shp'

    GISfile = every_dir + os.sep + 'GISfile'


    if not os.path.exists(GISfile):
        os.makedirs(GISfile)

    out_layer_or_view = GISfile + os.sep + name + "断面.shp"

    Output_polyline_features = GISfile + os.sep + name + "河网.shp"

    # gdb = work_space + os.sep + name + '.gdb'
    # start_('Kml_to_shp') #kml_转_shp
    # arcpy.KMLToLayer_conversion(kml, work_space)
    # poly = arcpy.SelectData_management(gdb, "Placemarks\Polylines")
    # end_('Kml_to_shp')
    #
    # start_('Project')   #投影
    # arcpy.Project_management(poly, incline, fill_dem)
    # end_('Project')

    start_('Fill')     #填洼
    arcpy.gp.Fill_sa(fill_dem, Output_surface_raster, "")
    end_('Fill')

    start_('Flow Direction')     #输出栅格流向
    arcpy.gp.FlowDirection_sa(Output_surface_raster, Output_flow_direction_raster, "NORMAL", "" , "D8")
    end_('Flow Direction')

    start_('Flow Accumulation')   #输出蓄积栅格
    arcpy.gp.FlowAccumulation_sa(Output_flow_direction_raster, Output_accumulation_raster, "", "FLOAT", "D8")
    end_('Flow Accumulation')

    start_('Con')  #筛选蓄积栅格
    Output_raster = Con(Raster(Output_accumulation_raster) >= 2000, 1)
    Output_raster.save(arcpy.env.workspace + os.sep + name + "_" + "Output_raster.tif")
    end_('Con')

    start_('Stream to Feature')   #生成河网
    arcpy.gp.StreamToFeature_sa(Output_raster, Output_flow_direction_raster, Output_polyline_features, "SIMPLIFY")
    end_('Stream to Feature')

    start_('Copy Feature')
    arcpy.CopyFeatures_management(shp, out_layer_or_view)
    end_('Copy Feature')


def main_(result_path, tem_path, dem_path, shp_path,tf):
    """
        Args:
            result_path: 结果文件夹
            tem_path：工作空间（临时文件夹）
            dem_path: 栅格tif文件及
            shp_path: 横断面shp数据文件夹
            tf:是否重复输出相同文件
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
        dem = dem_path + os.sep + name + '.tif'
        Process1(dem, line, tem_dir,result_path, name,tf)
        print ('Processed:\t', line)
        print "---------------------successful!!!!!!!!!!!!!!!-----------------------"

    print('---------------------------------all is ok----------------------------------------')

main_(result_path, tem_path, dem_path, shp_path,True)