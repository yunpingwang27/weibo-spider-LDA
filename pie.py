import pyecharts.options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType
import csv
# class _ThemeType:
    # BUILTIN_THEMES = ["light", "dark", "white"]
    # LIGHT = "light"
    # DARK = "dark"
    # WHITE = "white"
    # CHALK: str = "chalk"
    # ESSOS: str = "essos"
    # INFOGRAPHIC: str = "infographic"
    # MACARONS: str = "macarons"
    # PURPLE_PASSION: str = "purple-passion"
    # ROMA: str = "roma"
    # ROMANTIC: str = "romantic"
    # SHINE: str = "shine"
    # VINTAGE: str = "vintage"
    # WALDEN: str = "walden"
    # WESTEROS: str = "westeros"
    # WONDERLAND: str = "wonderland"
    # HALLOWEEN: str = "halloween"
# 请将下面的文件路径替换为你实际的CSV文件路径
file_path = 'keywords.txt'
keyword = []
with open(file_path, newline='',encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # print(row)
        keyword.append(row)
# 内部饼图
# 茅台,0.7402999084292129
# 酱香,0.6734627303831643
# 咖啡,0.508107745706493
# 视频,0.125178080847377
inner_x_data = ["茅台", '酱香','咖啡']
inner_y_data = [0.74,0.67,0.50]
# inner_x_data = ["直达", "营销广告", "搜索引擎","产品"]
# inner_y_data = [335, 679, 548, 283]
inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]
# [['直达', 335], ['营销广告', 679], ['搜索引擎', 1548], [‘产品’, 283]]
 
# 外部环形（嵌套）
# outer_x_data = ["贵州", "邮件营销", "直达", "营销广告", "联盟广告", "视频广告", "产品", "百度", "谷歌","邮件营销", "联盟广告"]
# outer_y_data = [335, 135, 147, 102, 220, 310, 234, 135, 648, 251]
# outer_data_pair = [list(z) for z in zip(outer_x_data, outer_y_data)]
#  
outer_data_pair = keyword[4:25]
c = (
     # 初始化
    Pie(init_opts=opts.InitOpts(
        width="900px",  # 设置图形大小
        height="800px",
        theme=ThemeType.WESTEROS))  # 选择主题
 
    # 内部饼图
    .add(
        series_name="内部",  # 图形名称
        center=["50%", "35%"],  # 饼图位置
        data_pair=inner_data_pair,  # 系列数据项，格式为 [(key1, value1), (key2, value2)]
        radius=["20%", "45%"],  # 饼图半径 数组的第一项是内半径，第二项是外半径
        label_opts=opts.LabelOpts(position='insideLeft'), # 标签设置在内部
    )
 
    # 外部嵌套环形图
    .add(
        series_name="外部",  # 系列名称
        center=["50%", "35%"],  # 饼图位置
        radius=["45%", "60%"],  # 饼图半径 数组的第一项是内半径，第二项是外半径
        data_pair=outer_data_pair, # 系列数据项，格式为 [(key1, value1), (key2, value2)]
 
        # 标签配置项 
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#f5f5f5",
            border_color="#ccc",
            font_family = 'Microsoft YaHei',
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999",
                      "lineHeight": 22,
                      "align": "center"},
 
                "abg": {
                    "backgroundColor": "#f0f0f0",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
 
 
                "hr": {
                    "borderColor": "#ccc",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
 
                "b": {"fontSize": 16, "lineHeight": 33},
 
                "per": {
                    "color": "#f5f5f5",
                    "backgroundColor": "#ddeeff",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
 
    # 全局配置项
    .set_global_opts(
        xaxis_opts = opts.AxisOpts(is_show = False),   #隐藏X轴刻度
        yaxis_opts = opts.AxisOpts(is_show = False),    #隐藏Y轴刻度
        # legend_opts = opts.LegendOpts(is_show = True),  #隐藏图例
        legend_opts = opts.LegendOpts(is_show = False),  #隐藏图例
        title_opts = opts.TitleOpts(title = '瑞幸联名'),    #隐藏标题
                    )
 
    # 系统配置项
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item",
            formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(is_show=True,position='inside',font_family='Microsoft YaHei')  # 隐藏每个触角标签
    )
)
 
c.render()