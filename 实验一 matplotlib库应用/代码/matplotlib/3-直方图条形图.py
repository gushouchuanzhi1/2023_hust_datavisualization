"""
3. 利用直方图和条形图绘制excel文件中current_prov对应的数据
（各省新冠疫情数据），要求使用多个子图，使用合适的视觉通道。
思考：哪一个图更为有效？
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

myfont = FontProperties(fname=r'G:\code\simfang.ttf')
df_prov = pd.read_excel(r'covid19_data.xls',sheet_name='current_prov')


# 创建子图
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# 设置子图标题
fig.suptitle('各省新冠疫情数据', fontsize=16, fontproperties=myfont)

# 绘制各省确诊人数条形图
axs[0, 0].bar(df_prov['province'], df_prov['confirm'], color='blue')
axs[0, 0].set_title('各省确诊人数', fontsize=12, fontproperties=myfont)
axs[0, 0].set_ylabel('人数', fontsize=10, fontproperties=myfont)

# 绘制各省死亡人数条形图
axs[0, 1].bar(df_prov['province'], df_prov['dead'], color='red')
axs[0, 1].set_title('各省死亡人数', fontsize=12, fontproperties=myfont)
axs[0, 1].set_ylabel('人数', fontsize=10, fontproperties=myfont)

# 绘制各省治愈人数条形图
axs[1, 0].bar(df_prov['province'], df_prov['heal'], color='green')
axs[1, 0].set_title('各省治愈人数', fontsize=12, fontproperties=myfont)
axs[1, 0].set_ylabel('人数', fontsize=10, fontproperties=myfont)

# 绘制各省疑似人数条形图
axs[1, 1].bar(df_prov['province'], df_prov['suspect'], color='purple')
axs[1, 1].set_title('各省疑似人数', fontsize=12, fontproperties=myfont)
axs[1, 1].set_ylabel('人数', fontsize=10, fontproperties=myfont)

# 设置横轴标签字体
for ax in axs.flat:
    ax.set_xlabel('省份', fontsize=10, fontproperties=myfont)
    ax.tick_params(axis='x', labelrotation=45)  # 旋转标签以防止重叠

# 调整子图之间的间距
plt.subplots_adjust(wspace=0.3, hspace=0.5)

# 显示图形
plt.show()