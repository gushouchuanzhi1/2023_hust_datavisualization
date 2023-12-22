'''
使用weibo.json中的数据绘制关系图，观察关系图的交互操作。
（提示：可以直接使用PPT中的代码）
'''

import json
from pyecharts import options as opts
from pyecharts.charts import Graph, Page
from pyecharts.charts import Graph, WordCloud, Bar, Pie, Page, Line

this_json = json.load(open('fixtures\\weibo.json', 'r', encoding='utf-8'))

# create nodes
nodes = [opts.GraphNode(
    name=_node['name'],
    symbol_size=_node['symbolSize'],
    value=_node['value'],
    category=_node['category']
) for _node in this_json[0]]

# create links
links = [opts.GraphLink(
    source=_link['source'],
    target=_link['target']
) for _link in this_json[1]]

# create categories
categories = [opts.GraphCategory(
    name=category
) for category in {_node['category']
                   for _node in this_json[0]}]

# create graph
graph = (Graph()
         .add("", nodes, links, categories, repulsion=50,
              linestyle_opts=opts.LineStyleOpts(curve=0.2),
              label_opts=opts.LabelOpts(is_show=False))
         .set_global_opts(legend_opts=opts.LegendOpts(is_show=False),
                          title_opts=opts.TitleOpts(title="Graph-微博关系图"))
         )
graph.render("out\\关系图.html")
