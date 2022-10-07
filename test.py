import csv
import filedialogs
with open('name.csv') as csv_file:
    FolderPath = filedialogs.open_folder_dialog('选择文件夹路径', 'gbk')
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