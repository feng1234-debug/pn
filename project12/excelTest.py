#coding=utf-8
#对文件的操作和读取
import xlrd
import os
import xlwt
from xlutils.copy import copy

def base_dir(filename=None):
    return os.path.join(os.path.dirname(__file__),filename)

# work=xlrd.open_workbook(base_dir('data.xls'))
# sheet=work.sheet_by_index(0)
#
# #查看多少行
# print(sheet.nrows)
#
# #获取到具体的内容
# print(sheet.cell_value(8,1))

'''excel文件内容的修改'''
work=xlrd.open_workbook(base_dir('data.xls'))
old_content=copy(work)
ws=old_content.get_sheet(0)
ws.write(9,3,'哈哈')
old_content.save(base_dir('excel.xls'))


