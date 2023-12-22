'''
对文件student.xls中的数据进行可视化：
（1）利用合适的条形图（堆叠或不堆叠）显示所有学生的总分；
（2）利用饼图展示总分前3名的分数构成；
（3）利用折线图显示英语，数分，高代，解几四门课程的成绩分布图（类似直方图，统计分数段内的人数，分数段按照每10分进行统计，然后用折线图展示)(
（4）利用合适地可视化图形展示男生和女生各科平均成绩的对比。
'''
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Page, Line
import pandas as pd
from pyecharts.commons.utils import JsCode

'''第一道题目'''


def text1(data_content):
    subjects = ['英语', '体育', '军训', '数分', '高代', '解几']

    bar = Bar(init_opts=opts.InitOpts(width='1260px', height='560px')) \
        .add_xaxis(data_content['姓名'].to_list())
    for subject in subjects:
        bar.add_yaxis(subject, [score for score in data_content[subject]], stack='same')
        bar.set_series_opts(label_opts=opts.LabelOpts(
            position="inside",
            formatter=JsCode("""
                judge(x) {
                    if (x.data > 0) return x.data;
                    else if (x.data == -1) return '未知';
                    else if (x.data == -2) return '作弊';
                    else return '缺考';
                }
            """)
        )
        ).set_global_opts(
            title_opts={'title': '学生总分'},
            xaxis_opts=opts.AxisOpts(name="姓名"),
            yaxis_opts=opts.AxisOpts(name="分数")
        )
    bar.render('out\\学生总分堆叠的条形图.html')


def text1plus(data_content):
    subjects = ['英语', '体育', '军训', '数分', '高代', '解几']
    data_content[data_content[subjects] < 0] = 0
    aa = [int(data_content.iloc[i, 4:].sum()) for i in range(data_content.shape[0])]
    bar = (
        Bar(init_opts=opts.InitOpts(width='1260px', height='560px'))
        .add_xaxis(data_content['姓名'].to_list())
        .add_yaxis('总分', aa)
        .set_global_opts(
            title_opts={'text': '学生总分'},
            xaxis_opts=opts.AxisOpts(name="姓名"),
            yaxis_opts=opts.AxisOpts(name="分数")
        )
    )

    bar.render('out\\学生总分不堆叠的条形图.html')


'''第二道题目'''


def text2(data_content):
    subjects = ['英语', '体育', '军训', '数分', '高代', '解几']
    total_sorted_top_three = sorted(
        enumerate(data_content[subjects].sum(axis=1)),
        key=lambda x: x[1],
        reverse=True
    )[:3]
    page = Page()
    for i in range(3):
        scores = data_content[subjects].iloc[total_sorted_top_three[i][0],].to_list()
        data = [opts.PieItem(name=subject, value=score) for subject, score in zip(subjects, scores)]
        pie = (
            Pie(init_opts=opts.InitOpts(width='1260px', height='560px')).add("", data)
            .set_series_opts(label_opts=opts.LabelOpts(position='inside', formatter='{b}:{c}'))
            .set_global_opts(
                title_opts={"text": "学生分数构成", "subtext": f"第{i + 1}名 总分：{total_sorted_top_three[i][1]}"})
        )
        page.add(pie)
    page.render("out\\饼图学生成绩前三.html")


'''第三道题目'''


def text3(data_content):
    subjects = ['英语', '数分', '高代', '解几']
    line = (
        Line(init_opts=opts.InitOpts(width='1260px', height='560px'))
        .add_xaxis(list(range(0, 101, 10)))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="成绩分布图"),
            legend_opts=opts.LegendOpts(is_show=True)
        )
    )
    for subject in subjects:
        data = [0] * 11
        for score in data_content[subject]:
            data[score // 10] += 1
        line.add_yaxis(subject, [opts.LineItem(name="人数", value=num) for num in data])
    line.render("out\\四门课程成绩分布图.html")


'''第四道题目'''


def text4(data_content):
    subjects = ['英语', '体育', '军训', '数分', '高代', '解几']
    male = []
    female = []
    for index, gender in enumerate(data_content['性别']):
        if gender == '男':
            male.append(index)
        else:
            female.append(index)

    subject_ave_male = []
    subject_ave_female = []
    for subject in subjects:
        subject_ave_male.append(round(data_content[subject][male].mean(), 2))
        subject_ave_female.append(round(data_content[subject][female].mean(), 2))

    bar = (
        Bar(init_opts=opts.InitOpts(width='1260px', height='560px'))
        .add_xaxis(subjects)
        .add_yaxis('男生', subject_ave_male)
        .add_yaxis('女生', subject_ave_female)
        .set_global_opts(
            title_opts={'text': '男女各科平均分对比'},
            xaxis_opts=opts.AxisOpts(name="科目"),
            yaxis_opts=opts.AxisOpts(name="分数")
        )
    )

    bar.render('out\\男女各科的平均成绩对比.html')


if __name__ == '__main__':
    situation = {'未知': -1, '作弊': -2, '缺考': -3}
    # 处理未知的数据
    data = pd.read_excel(pd.ExcelFile('fixtures\\student.xls'), sheet_name='Sheet1').fillna(situation['未知']).replace(situation)
    text1(data)
    text1plus(data)
    text2(data)
    text3(data)
    text4(data)
