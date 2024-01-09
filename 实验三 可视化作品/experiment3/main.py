import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def draw1(df):  # 绘制2019年各省份订购数量饼图
    # 统计各省份数量
    province_counts = df['所在省份'].value_counts()
    myfont = FontProperties(fname=r'G:\code\simfang.ttf')

    # 绘制饼图
    plt.figure(figsize=(8, 8))
    plt.pie(province_counts, labels=province_counts.index, autopct='%1.1f%%', startangle=45,
            textprops={'fontproperties': myfont})
    plt.title('2019年各省份订购数量图', fontproperties=myfont)
    plt.savefig('out//2019年各省份订购数量饼图.png')
    # plt.show()


def draw2(df):  # 绘制2019年各地区订购数量饼图
    # 统计各地区数量
    province_counts = df['所在区域'].value_counts()
    myfont = FontProperties(fname=r'G:\code\simfang.ttf')

    # 绘制饼图
    plt.figure(figsize=(8, 8))
    plt.pie(province_counts, labels=province_counts.index, autopct='%1.1f%%', startangle=45,
            textprops={'fontproperties': myfont})
    plt.title('2019年各地区订购数量图', fontproperties=myfont)
    plt.savefig('out//2019年各地区订购数量饼图.png')
    # plt.show()


def draw3(df):  # 各月份的订购数量变化折线图
    myfont = FontProperties(fname=r'G:\code\simfang.ttf')
    # 将日期列转换为日期类型
    df['订单日期'] = pd.to_datetime(df['订单日期'])
    df['订购数量'] = pd.to_numeric(df['订购数量'], errors='coerce')
    # 按月份分组并求和
    monthly_data = df.groupby(df['订单日期'].dt.to_period("M").astype(str)).agg({'订购数量': 'sum'}).reset_index()
    # 绘制折线图
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_data['订单日期'], monthly_data['订购数量'], marker='o')
    plt.title('每月订购数量折线图', fontsize=14, fontproperties=myfont)
    plt.xlabel('月份', fontsize=14, fontproperties=myfont)
    plt.ylabel('订购数量', fontsize=14, fontproperties=myfont)
    plt.ticklabel_format(style='plain', axis='y')
    plt.savefig('out//各月份的总化妆品订购数量变化折线图')


def draw4(df):
    myfont = FontProperties(fname=r'G:\code\simfang.ttf')
    # 按地区和商品小类分组，并计算购买数量总和
    df['订购数量'] = pd.to_numeric(df['订购数量'], errors='coerce')  # 同draw3进行处理
    grouped_data = df.groupby(['所在区域', '商品小类']).agg({'订购数量': 'sum'}).reset_index()
    selected_regions = ['东区', '西区', '南区', '北区']
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'yellow']
    for i, region in enumerate(selected_regions):
        region_data = grouped_data[grouped_data['所在区域'] == region]
        plt.figure(figsize=(8, 8))
        plt.pie(region_data['订购数量'], labels=region_data['商品小类'], autopct='%1.1f%%', startangle=90,
                textprops={'fontproperties': myfont}, colors=colors)
        plt.title(f'{region}购买商品的商品小类分布', fontsize=14, fontproperties=myfont)
        plt.savefig(f'out//商品小类分布//{region}购买商品的商品小类分布')
        # plt.show()


def draw5(df):
    myfont = FontProperties(fname=r'G:\code\simfang.ttf')
    # 按地区和商品小类分组，并计算购买数量总和
    df['订购数量'] = pd.to_numeric(df['订购数量'], errors='coerce')  # 同draw3进行处理
    grouped_data = df.groupby(['所在区域', '商品大类']).agg({'订购数量': 'sum'}).reset_index()
    selected_regions = ['东区', '西区', '南区', '北区']
    for region in selected_regions:
        # 选择当前区域的数据
        region_data = grouped_data[grouped_data['所在区域'] == region]

        # 绘制饼图
        plt.figure(figsize=(8, 8))
        plt.pie(region_data['订购数量'], labels=region_data['商品大类'], autopct='%1.1f%%', startangle=90,
                textprops={'fontproperties': myfont})
        plt.title(f'{region}购买商品的商品大类分布', fontsize=14, fontproperties=myfont)
        plt.savefig(f'out//商品大类分布//{region}购买商品的商品大类分布')
        # plt.show()


def draw6(df):
    myfont = FontProperties(fname=r'G:\code\simfang.ttf')
    df['订购数量'] = pd.to_numeric(df['订购数量'], errors='coerce')
    product_categories = ['面膜', '眼霜', '面霜', '洁面乳', '爽肤水', '隔离霜', '防晒霜', '口红', '粉底', '眼影',
                          '睫毛膏', '蜜粉']
    for category in product_categories:
        temp = df['商品小类'] == category
        temp_data = df[temp]
        category_data = temp_data.groupby('所在省份')['订购数量'].sum().reset_index()
        # 绘制柱状图
        plt.figure(figsize=(12, 6))
        plt.bar(category_data['所在省份'], category_data['订购数量'], color='skyblue')
        plt.title(f'各省份订购{category}数量统计', fontproperties=myfont)
        plt.xlabel('省份', fontsize=10, fontproperties=myfont)
        plt.ylabel('订购数量', fontsize=10, fontproperties=myfont)
        plt.ticklabel_format(style='plain', axis='y')  # 避免使用科学计数法
        plt.tick_params(axis='x', labelrotation=45)
        plt.savefig(f'out//商品小类订购数量//{category}的各省份订购数量条形图.png')
        plt.close()  # 关闭当前图表，避免下一次循环时重叠


def draw7(df):
    myfont = FontProperties(fname=r'G:\code\simfang.ttf')
    product_categories = ['面膜', '眼霜', '面霜', '洁面乳', '爽肤水', '隔离霜', '防晒霜', '口红', '粉底', '眼影',
                          '睫毛膏', '蜜粉']

    merged_df['订单日期'] = pd.to_datetime(merged_df['订单日期'])
    df_2019 = merged_df[merged_df['订单日期'].dt.year == 2019]

    df_2019['订购数量'] = pd.to_numeric(df_2019['订购数量'], errors='coerce')
    plt.figure(figsize=(12, 6))
    for category in product_categories:
        mask = df_2019['商品小类'] == category
        category_data = df_2019[mask].groupby('商品小类')['订购数量'].sum().reset_index()
        plt.bar(category_data['商品小类'], category_data['订购数量'], label=category, color='skyblue')
    plt.title('2019年各商品小类订购数量统计', fontproperties=myfont)
    plt.xlabel('商品小类', fontsize=12, fontproperties=myfont)
    plt.ylabel('订购数量', fontsize=12, fontproperties=myfont)
    plt.ticklabel_format(style='plain', axis='y')  # 避免使用科学计数法
    plt.legend()  # 显示图例
    plt.savefig('out//2019年各商品小类订购数量统计图')


def draw8(df):
    myfont = FontProperties(fname=r'G:\code\simfang.ttf')
    product_categories = ['面膜', '眼霜', '面霜', '洁面乳', '爽肤水', '隔离霜', '防晒霜', '口红', '粉底', '眼影',
                          '睫毛膏', '蜜粉']
    # 将日期列转换为日期类型
    df['订单日期'] = pd.to_datetime(df['订单日期'])
    df['年份'] = df['订单日期'].dt.year
    df['月份'] = df['订单日期'].dt.month
    df['订购数量'] = pd.to_numeric(df['订购数量'], errors='coerce')
    # 使用 pivot_table 将数据透视，以商品小类和月份为索引
    pivot_data = df.pivot_table(index=['年份', '月份'], columns='商品小类', values='订购数量', aggfunc='sum',
                                       fill_value=0)
    pivot_data.reset_index(inplace=True)
    plt.figure(figsize=(15, 6))
    for category in product_categories:
        plt.plot(pivot_data['月份'], pivot_data[category], label=category)
    plt.title('2019年各月份订购数量折线图', fontproperties=myfont)
    plt.xlabel('月份', fontproperties=myfont)
    plt.ylabel('订购数量', fontproperties=myfont)
    plt.ticklabel_format(style='plain', axis='y')  # 避免使用科学计数法
    plt.legend(prop=myfont)
    plt.savefig('out//2019年各商品小类每月订购变化图')


if __name__ == '__main__':
    file_path = '日化.xlsx'
    df1 = pd.read_excel(file_path, sheet_name=0)
    df2 = pd.read_excel(file_path, sheet_name=1)
    merged_df = pd.merge(df1, df2, on='商品编号', how='inner')
    draw1(df1)  # 绘制2019年各省份订购数量饼图
    draw2(df1)
    draw3(df1)
    draw4(merged_df)
    draw5(merged_df)
    draw6(merged_df)
    draw7(merged_df)
    draw8(merged_df)
