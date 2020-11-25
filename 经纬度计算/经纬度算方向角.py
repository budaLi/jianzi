import math
import xlrd
from xlutils.copy import copy as xl_copy


def geoDistance(lng1, lat1, lng2, lat2):
    '''
    公式计算两点间距离（m）
    '''
    # 经纬度转换成弧度
    lng1, lat1, lng2, lat2 = map(math.radians, [float(lng1), float(lat1), float(lng2), float(lat2)])
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    distance = 2 * math.asin(math.sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
    distance = round(distance, 3)
    return distance


def geoDegree(lng1, lat1, lng2, lat2):
    '''
    公式计算两点间方位角
    方位角：是与正北方向、顺时针之间的夹角
    '''
    lng1, lat1, lng2, lat2 = map(math.radians, [float(lng1), float(lat1), float(lng2), float(lat2)])
    dlon = lng2 - lng1
    y = math.sin(dlon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    brng = math.degrees(math.atan2(y, x))
    brng = (brng + 360) % 360
    return brng



class OperationExcel():
    """
    操作Excel
    """

    def __init__(self, file_name=None, sheet_id=None):
        """
        初始化OperationExcel对象
        :param file_name:
        :param sheet_id: vv
        """
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            raise Exception("请指定filename")
        self.tables = self.get_tables()

    def get_tables(self):
        """
        返回tables对象
        :return:
        """
        ecel = xlrd.open_workbook(self.file_name)
        tables = ecel.sheet_by_index(self.sheet_id)
        return tables

    def get_nrows(self):
        """
        获取表格行数
        :return:
        """
        return self.tables.nrows

    def get_ncols(self):
        """
        获取表格列数
        :return:
        """
        return self.tables.ncols


    def get_cel_value(self, row, col):
        """
        获取某个指定单元格的内容
        :param row:
        :param col:
        :return:
        """
        data = self.tables.cell_value(row, col)
        return data

    def write_to_excel(self, file_path, sheet_id, row, col, value):
        """
        写入excel
        """
        work_book = xlrd.open_workbook(file_path, formatting_info=False)
        # 先通过xlutils.copy下copy复制Excel
        write_to_work = xl_copy(work_book)
        # 通过sheet_by_index没有write方法 而get_sheet有write方法
        sheet_data = write_to_work.get_sheet(sheet_id)
        sheet_data.write(row, col, str(value))
        # 这里要注意保存 可是会将原来的Excel覆盖 样式消失
        write_to_work.save(file_path)

def main():
    file_path ="20190401OD经纬度.xlsx"
    res_file = "res.xls"

    operation_excel = OperationExcel(file_path,0)
    address_col = 0
    lon_col = 1
    lat_col = 2

    # 多少行
    totle_numbers = operation_excel.get_nrows()

    totle_res = []
    for i in range(2,totle_numbers):
        address = operation_excel.get_cel_value(i,address_col)
        lon = operation_excel.get_cel_value(i,lon_col)
        lat = operation_excel.get_cel_value(i,lat_col)
        tem = [address,lon,lat]
        totle_res.append(tem)

    count = 0
    for i in range(len(totle_res)):
        for j in range(len(totle_res)):
            if i==j:
                continue
            address1= totle_res[i][0]
            lon1 = totle_res[i][1]
            lat1 = totle_res[i][2]

            address2 = totle_res[j][0]
            lon2 = totle_res[j][1]
            lat2 = totle_res[j][2]
            degree = geoDegree(lon1,lat1,lon2,lat2)
            distance = geoDistance(lon1,lat1,lon2,lat2)

            print("{}:{}，{}，degree:{},distance:{}".format(i,address1,address2,degree,distance))
            operation_excel.write_to_excel(res_file,0,count,0,address1+","+address2)
            operation_excel.write_to_excel(res_file,0,count,1,degree)
            operation_excel.write_to_excel(res_file,0,count,2,distance)
            count+=1

if __name__ == '__main__':
    main()

