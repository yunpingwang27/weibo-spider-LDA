import jieba
import re
import csv
 
import jieba.analyse

import pandas as pd

# 读取CSV文件
data = pd.read_csv("结果文件/瑞幸联名/瑞幸联名.csv")

# 获取第5列数据
column_5 = data.iloc[:, 4]

print(column_5)

# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open('./hit_stopwords.txt',encoding='UTF-8').readlines()]
    return stopwords
 
def processing(text):
    """
    数据清洗, 可以根据自己的需求进行重载
    """
    text = re.sub("@.+?( |$)", "", text)           # 去除 @xxx (用户名)
    text = re.sub("【.+?】", "", text)             # 去除 【xx】 (里面的内容通常都不是用户自己写的)
    text = re.sub(".*?:", "", text)                #去除微博用户的名字
    text = re.sub("#.*#", "", text)                #去除话题引用
    text = re.sub("\n","",text)
    return text
 
# 对句子进行中文分词
def seg_depart(sentence):
    jieba.load_userdict('./保留词.txt')
    sentence_depart = jieba.cut(sentence.strip())
    # print(sentence_depart)
    stopwords = stopwordslist()        # 创建一个停用词列表
    outstr = ''        # 输出结果为outstr
    for word in sentence_depart:          # 去停用词
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += "/"
    return outstr
 
# 给出文档路径
# filename = "结果文件/瑞幸联名/瑞幸联名.csv"   #原文档路径
outputs = open("./output.csv", 'w', encoding='UTF-8')  #输出文档路径
# with open(filename, 'r', encoding='utf-8-sig') as csvfile:
    # reader = csv.reader(csvfile,delimiter=',',quotechar='"',doublequote=False)
s = ''
for line in list(column_5):
    # print(line[0])     #微博在文档的第一列
    s = s+ str(line)
    # print(s)
    line = processing(line)
    line_seg = seg_depart(line)
    outputs.write(line_seg + '\n')
keywords = jieba.analyse.extract_tags(
    sentence= s,    # 文本内容
    topK=100,          # 提取的关键词数量
    # allowPOS=['n','nz','v', 'vd', 'vn', 'ns', 'nr'],  # 允许的关键词的词性
    allowPOS=['n','nz', 'vd', 'ns', 'nr'],  # 允许的关键词的词性
    withWeight=True,  # 是否附带词语权重
    # withFlag=True,    # 是否附带词语词性
    )
    # result = jieba.analyse.extract_tags(text,topK = n,withWeight = True,allowPOS=('nr',))
# result[:10] #打印前10个人物
outputs.close()
print("分词成功！！！")
# print(keywords)
# 打开一个txt文件进行写入

with open('keywords.txt', 'w',encoding = 'utf-8') as file:
    for item in keywords:
        # for i in item:
        file.write(f'{item[0]},{item[1]}\n')

print("内容已成功写入到keywords.txt文件中！")





# 词云分析
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# from imageio import imreads
import jieba
keyword = dict()#关键词
for i in keywords:
    keyword[i[0]] = i[1]
#设置词云属性
from PIL import Image
import numpy as np
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
image = Image.open('./cup.jpg')
graph = np.array(image)
wc  = WordCloud(font_path='./simhei.ttf',background_color = 'white',max_words = 100,mask = graph)#字体，背景颜色，词云显示最大词数，背景样式
wc.generate_from_frequencies(keyword)
plt.imshow(wc)
image_color=ImageColorGenerator(graph)
plt.imshow(wc.recolor(color_func = image_color))
plt.axis("off")
plt.show()
wc.to_file('词云.jpg')

