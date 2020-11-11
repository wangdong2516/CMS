# # """操作excel"""
# # from datetime import datetime
# #
# # import xlwt
# #
# # # 创建一个workbook并且设置编码
# # workbook = xlwt.Workbook(encoding='utf-8')
# #
# # # 创建一个worksheet
# # worksheet = workbook.add_sheet('测试')
# #
# # data_list = [
# #     '姓名', '年龄', '家庭地址', '联系方式', '备注'
# # ]
# #
# # # 设置单元格的样式
# # style = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
# #     num_format_str='#,##0.00')
# # alignment = xlwt.Alignment() # Create Alignment
# # alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
# # alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
# # style.alignment = alignment # Add Alignment to Style
# # style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
# # # 写入表头数据
# # for index, item in enumerate(data_list):
# #     # 带样式的写入
# #     worksheet.write(0, index, item, style)
# #
# # value_list = [
# #     ['王栋', '26', '北京市', '18734872516', 'python工程师'],
# #     ['王栋', '26', '北京市', '18734872516', 'python工程师'],
# #     ['王栋', '26', '北京市', '18734872516', 'python工程师'],
# #     ['王栋', '26', '北京市', '18734872516', 'python工程师'],
# # ]
# #
# #
# # for s, i in enumerate(value_list):
# #     for pos, item in enumerate(i):
# #         worksheet.write(s + 1, pos, item, style=style)
# # # worksheet.write(2, 0, 1)
# # # worksheet.write(2, 1, 1)
# #
# #
# # # 计算公式
# # # worksheet.write(2, 2, xlwt.Formula("A3+B3"))
# #
# # # 保存数据
# # workbook.save('测试.xls')
#
#
# from openpyxl import Workbook
# from openpyxl import load_workbook
# # 生成workbook工作簿
# wb = Workbook()
#
# # 获取一个sheet
# ws = wb.active
#
# # 默认的sheet的名称是sheet，这里进行修改
# ws.title = '测试2'
#
# # 增加其他的sheet
# wb.create_sheet('sheet2')
# wb.create_sheet('sheet3')
# wb.create_sheet('sheet4')
#
# # 赋值给A1单元格
# ws['A1'] = 42
# ws.sheet_properties.tabColor = '1072BA'
# # 写入下一行
# ws.append([1, 2, 3])
#
# # 获取某一个sheet
# s1 = wb['sheet2']
# print(s1)
#
# # 创建sheet的副本，新的sheet的名称将会是sheet Copy
# wb.copy_worksheet(s1)
#
# # 遍历工作薄
# for i in wb:
#     print(i)
#
# # 获取所有sheet的名称
# print(wb.sheetnames)
#
# # 修改单元格的内容
# ws['A4'] = '小店区'
#
# # 使用行和列的形式修改单元格,效果等同于ws['A4'] = '小店区'
# ws.cell(4, 1, value="刘家堡")
#
# print([x.value for x in ws['C']])
#
# # 访问单元格的范围
# # r = ws['A1': 'C2']
# r = ws[1: 5]
# print(r)
#
# # 保存文件
# wb.save('测试2.xlsx')
#
# # 读取xls文件
# wb2 = load_workbook('测试2.xlsx')
# print(wb2.sheetnames)
#
#
# from openpyxl import Workbook
# from openpyxl.utils import get_column_letter
#
# wb = Workbook()
#
# dest_filename = 'empty_book.xlsx'
#
value_list = [
    ['王栋', '26', '北京市', '18734872516', 'python工程师'],
    ['王栋', '26', '北京市', '18734872516', 'python工程师'],
    ['王栋', '26', '北京市', '18734872516', 'python工程师'],
    ['王栋', '26', '北京市', '18734872516', 'python工程师'],
]
# ws1 = wb.active
# ws1.title = "range names"
#
# # for row in range(1, 40):
# #     ws1.append(range(600))
#
# for data in value_list:
#     ws1.append(data)
#
#
# ws2 = wb.create_sheet(title="Pi")
#
# ws2['F5'] = 3.14
#
# # 合并单元格
# ws1.merge_cells('A2:D3')
#
# # 新增一个sheet
# ws3 = wb.create_sheet(title="Data")
# for row in range(10, 20):
#     for col in range(27, 54):
#         _ = ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
# print(ws3['AA10'].value)
#
# wb.save(filename = dest_filename)
