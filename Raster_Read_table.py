<<<<<<< HEAD
# coding:utf-8
#功能：批量导出栅格文件的属性表。
#使用步骤 1：在相应文件夹下新建“文件地理数据库”，并将需要导出属性表的栅格文件“导入”到该数据库中。
#使用步骤 2：更改第二行代码[ws = r'D:\test\test.gdb']为自己的文件存放地址和数据库名称，第三行同样的处理。
#使用步骤 3：复制代码在ArcGIS中运行即可。
import arcpy, os
ws = r'D:\sort_mask_out\out_table.gdb'
outCSV = r'C:\Users\Administrator\Desktop\sort_interset.csv'
arcpy.env.workspace = ws
rasters = arcpy.ListRasters("*")
for raster in rasters:
    rasloc = ws + os.sep + raster
    fields = "*"
    try:
        lstFlds = arcpy.ListFields(rasloc)   #获取栅格数据的字段
        header = ''
        header += ",{0}".format(lstFlds[0].name)+",{0}".format(lstFlds[1].name)
        if len(lstFlds) != 0:
            f = open(outCSV,'a')
            header = header[0:] + ',RasterName\n'
            f.write(header)
            with arcpy.da.SearchCursor(rasloc, fields) as cursor:
                for row in cursor:
                    f.write(str(row).replace("(","").replace(")","") + "," + raster + '\n')
            f.close()
    except Exception as e:
        print (e)
=======
# coding:utf-8
#功能：批量导出栅格文件的属性表。
#使用步骤 1：在相应文件夹下新建“文件地理数据库”，并将需要导出属性表的栅格文件“导入”到该数据库中。
#使用步骤 2：更改第二行代码[ws = r'D:\test\test.gdb']为自己的文件存放地址和数据库名称，第三行同样的处理。
#使用步骤 3：复制代码在ArcGIS中运行即可。
import arcpy, os
ws = r'D:\sort_mask_out\out_table.gdb'
outCSV = r'C:\Users\Administrator\Desktop\sort_interset.csv'
arcpy.env.workspace = ws
rasters = arcpy.ListRasters("*")
for raster in rasters:
    rasloc = ws + os.sep + raster
    fields = "*"
    try:
        lstFlds = arcpy.ListFields(rasloc)   #获取栅格数据的字段
        header = ''
        header += ",{0}".format(lstFlds[0].name)+",{0}".format(lstFlds[1].name)
        if len(lstFlds) != 0:
            f = open(outCSV,'a')
            header = header[0:] + ',RasterName\n'
            f.write(header)
            with arcpy.da.SearchCursor(rasloc, fields) as cursor:
                for row in cursor:
                    f.write(str(row).replace("(","").replace(")","") + "," + raster + '\n')
            f.close()
    except Exception as e:
        print (e)
>>>>>>> 50a0148 (first commit)
del row