"""
2. 利用饼图绘制excel文件中data_world对应的数据（各国新冠疫情数据），
要求显示确诊人数最多的前4个国家的confirm，dead、heal和suspect的分布饼图。
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties
#指定中文字库
myfont = FontProperties(fname=r'G:\code\simfang.ttf')

df = pd.read_excel(r'covid19_data.xls', sheet_name='data_world')
df_sorted = df.sort_values(by='confirm', ascending=False)  ##由于是降序排序，所以ascending=False
df_countries = df_sorted.head(4)

label = df_countries['country']
confirm_data = df_countries['confirm']
dead_data = df_countries['dead']
heal_data = df_countries['heal']
suspect_data = df_countries['suspect']

# 绘制分布饼图 一共四张子图2 2的坐标分布
fig, axs = plt.subplots(2, 2, figsize=(20, 20))

# 确诊人数分布
axs[0, 0].pie(confirm_data, labels=label, autopct='%1.1f%%', startangle=90, textprops={'fontproperties': myfont})
axs[0, 0].set_title('确诊人数分布', fontproperties=myfont)

# 死亡人数分布
axs[0, 1].pie(dead_data, labels=label, autopct='%1.1f%%', startangle=90, textprops={'fontproperties': myfont})
axs[0, 1].set_title('死亡人数分布', fontproperties=myfont)

# 治愈人数分布
axs[1, 0].pie(heal_data, labels=label, autopct='%1.1f%%', startangle=90, textprops={'fontproperties': myfont})
axs[1, 0].set_title('治愈人数分布', fontproperties=myfont)

# 疑似人数分布
axs[1, 1].pie(suspect_data, labels=label, autopct='%1.1f%%', startangle=90, textprops={'fontproperties': myfont})
axs[1, 1].set_title('疑似人数分布', fontproperties=myfont)

plt.show()
