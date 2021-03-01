# -*- coding:utf-8 _*-
""" 
@file: pd_write_excel.py 
@time: 2021/03/01
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""
'''
将 字典列表 写入到Excel中
'''

import xlwt
import pandas as pd

data_list = [
    {
        'request_time': '2021-03-01 15:08:20',
        'picture_name': './test-sample/stick-holding/be87162c6af4.jpg',
        'detect_result': {'code': 0, 'msg': '操作成功', 'data': {'type': 0, 'Param': '', 'similarity': '1'}}
    },
    {
        'request_time': '2021-03-01 15:08:21',
        'picture_name': './test-sample/stick-holding/c76117c0ef77484bacf55634f0566215.jpeg',
        'detect_result': {'code': 0, 'msg': '操作成功', 'data': {'type': 0, 'Param': '', 'similarity': '1'}}
    },
    {
        'request_time': '2021-03-01 15:08:21',
        'picture_name': './test-sample/stick-holding/csGR32.jpg',
        'detect_result': {'code': 0, 'msg': '操作成功', 'data': {'type': 0, 'Param': '', 'similarity': '1'}}
    },
    {
        'request_time': '2021-03-01 15:08:22',
        'picture_name': './test-sample/stick-holding/fyssmmc6046525.jpg',
        'detect_result': {'code': 0, 'msg': '操作成功', 'data': {'type': 4, 'Param': '', 'similarity': 87.25}}
    },
    {
        'request_time': '2021-03-01 15:08:22',
        'picture_name': './test-sample/stick-holding/fyssmmc6047047.jpg',
        'detect_result': {'code': 0, 'msg': '操作成功', 'data': {'type': 4, 'Param': '', 'similarity': 88.66}}
    },
    {
        'request_time': '2021-03-01 15:08:23',
        'picture_name': './test-sample/stick-holding/Img261127079.jpg',
        'detect_result': {'code': 0, 'msg': '操作成功', 'data': {'type': 4, 'Param': '', 'similarity': 81.18}}
    },
    {
        'request_time': '2021-03-01 15:08:24',
        'picture_name': './test-sample/stick-holding/Img274604447.jpg',
        'detect_result': {'code': 0, 'msg': '操作成功', 'data': {'type': 2, 'Param': '', 'similarity': 78.37}}
    },
    {
        'request_time': '2021-03-01 15:08:24',
        'picture_name': './test-sample/stick-holding/Img379194304.jpg',
        'detect_result': {'code': 0, 'msg': '操作成功', 'data': {'type': 4, 'Param': '', 'similarity': 87.18}}
    },
    {
        'request_time': '2021-03-01 15:08:25',
        'picture_name': './test-sample/stick-holding/Img407597286.jpg',
        'detect_result': {'code': 0, 'msg': '操作成功', 'data': {'type': 4, 'Param': '', 'similarity': 84.94}}
    },
    {
        'request_time': '2021-03-01 15:08:26',
        'picture_name': './test-sample/stick-holding/U11366P1T1D30472101F21DT20140705181422.jpg',
        'detect_result': {'code': 0, 'msg': '操作成功', 'data': {'type': 0, 'Param': '', 'similarity': '1'}}
    },
]


def export_excel(export: list, file_name):
    # 将字典列表转换为DataFrame
    pf = pd.DataFrame(list(export))
    # 指定字段顺序
    order = ['request_time', 'picture_name', 'detect_result']
    pf = pf[order]
    # 将列名替换为中文
    columns_map = {
        'request_time': '请求时间',
        'picture_name': '图片名称',
        'detect_result': '检测结果',
    }
    pf.rename(columns=columns_map, inplace=True)
    # 指定生成的Excel表格名称
    file_path = pd.ExcelWriter(f'{file_name}.xlsx')
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    # 保存表格
    file_path.save()


if __name__ == '__main__':
    # 将分析完成的列表导出为excel表格
    export_excel(data_list, 'result')
