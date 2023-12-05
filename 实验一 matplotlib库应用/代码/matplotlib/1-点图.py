"""
1. 利用折线图和散点图绘制excel文件中data_history对应的数据（按日期的新冠疫情数据），
要求分别在折线图和散点图上显示confirm，dead和heal数据，使用不同的视觉通道（样式、颜色等）。
注意：（1）中文标注的使用；（2）xticks和yticks对坐标轴的处理。
思考：哪一个图更为有效？
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 读取Excel文件
df = pd.read_excel(r'covid19_data.xls', sheet_name='data_history')

# 将日期列设置为索引
df.set_index('date', inplace=True)

# 筛选数据，仅包含指定日期范围内的数据
start_date = '2020-01-20'
end_date = '2020-02-25'
df = df[start_date:end_date]

# 重新转换索引为日期格式
df.index = pd.to_datetime(df.index)

# 指定中文字体
myfont = FontProperties(fname=r'G:\code\simfang.ttf')

# 创建散点图
fig, ax = plt.subplots(figsize=(15, 6))

# 绘制散点图
ax.scatter(df.index, df['confirm'], label='确诊', color='blue', marker='o')
ax.scatter(df.index, df['dead'], label='死亡', color='red', marker='s')
ax.scatter(df.index, df['heal'], label='治愈', color='green', marker='^')
ax.scatter(df.index, df['suspect'], label='疑似', color='purple', marker='d')

# 设置中文标签
ax.set_title('新冠疫情数据', fontsize=16, fontproperties=myfont)
ax.set_xlabel('日期', fontsize=14, fontproperties=myfont)
ax.set_ylabel('人数', fontsize=14, fontproperties=myfont)

# 设置日期显示格式
ax.xaxis.set_major_locator(plt.MaxNLocator(37))  # 设置37个刻度，即每一天一个刻度
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))  # 日期格式为年-月-日

# 添加图例
ax.legend(prop=myfont)

# 显示xticks斜体
plt.xticks(rotation=45)

# 显示图形
plt.show()
