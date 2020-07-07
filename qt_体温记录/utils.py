# @Time    : 2020/6/23 11:03
# @Author  : Libuda
# @FileName: utils.py
# @Software: PyCharm
import xlrd
from xlutils.copy import copy


def get_keywords_data(tables, row, col):
    actual_data = tables.cell_value(row, col)
    return actual_data

def write_to_excel(file_path, row, col, value):
    work_book = xlrd.open_workbook(file_path, formatting_info=False)
    write_to_work = copy(work_book)
    sheet_data = write_to_work.get_sheet(0)
    sheet_data.write(row, col, str(value))
    write_to_work.save(file_path)