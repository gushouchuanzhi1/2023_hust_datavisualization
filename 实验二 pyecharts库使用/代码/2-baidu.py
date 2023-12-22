import json
import requests
from pyecharts import options as opts
from pyecharts.charts import WordCloud

# 首先要爬取数据，每个热搜的数据
url = 'https://top.baidu.com/api/board?platform=wise&tab=realtime&tag=%7B%7D'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.51 Safari/537.36',
    'Host': 'top.baidu.com',
    'Accept': 'application / json, text / plain, * / *',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
}
# 向网页申请，爬取数据
resp = requests.get(url, headers=header)
# 保存爬取的数据
content = json.loads(resp.text)['data']['cards'][0]['content']
# 只要求爬取前20条
titles = [item['query'] for item in content][:20]
words = [(title, len(titles) - index) for index, title in enumerate(titles)]
# 生成词云
wordcloud = (WordCloud(init_opts=opts.InitOpts(width='1600px', height='650px'))
             .add("", words, word_size_range=[5, 100])
             .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-百度热搜榜前20")))
wordcloud.render('out\\百度热搜.html')
