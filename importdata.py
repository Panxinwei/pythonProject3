import csv

import numpy as np
import  pandas as pd
from filedialogs import filedialogs
from numpy import ma


def getimportdata(self):
    FolderPath = filedialogs.open_file_dialog('选择文件夹路径', 'gbk')

    '''with open(FolderPath) as csv_file:
        # 创建一个 CSV Reader 对象
        reader = csv.reader(csv_file)
        # 设置行数所以我们知道哪一行的标题
        line_count = 0
        for row in reader:
            # 从文件的第一行打印出标题
            if line_count == 0:
                print(f'列标题是: {", ".join(row)}')
                line_count += 1
            # 从剩余的行中打印出数据
            else:
                print(f'{row[0]}，住在 {row[1]}，{row[2]}, 出生日期是 {row[3]}。')
                line_count += 1
        print(f'CSV文件一共有 {line_count} 行')
        '''
    input_data = pd.read_csv(FolderPath,

                             usecols=['TestName', 'InstrumentName', 'ResultValueTime', 'ResultValue', 'ResultValueDate'],

                             parse_dates=['ResultValueTime'])

    pd.set_option('expand_frame_repr', False)
    # 将数据按照交易日期从远到近排序

    input_data = input_data.sort_values(by='ResultValueTime', ascending=1)

    # ========== 计算移动平均线(以‘前复权价’为例)

    # 分别计算5日、20日、60日的移动平均线
  #  ListMA = input_data['ResultValue'].rolling(5).mean().values
  #  arrMA = np.array(ListMA)
  #  print(arrMA)


    return input_data