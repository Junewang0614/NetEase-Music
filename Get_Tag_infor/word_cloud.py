import wordcloud
import jieba
from scipy.misc import imread
def makeclouds():
    f = open("result1.txt", 'r', encoding='utf-8').read()
    txt=f
    txt=" ".join(jieba.lcut(txt))
    mk=imread("cat.jpg")
    w=wordcloud.WordCloud(width=600,
                          height=400,
                          min_font_size=20,
                          max_font_size=50,
                          font_path="msyh.ttc",
                          mask=mk,
                          background_color="white"
                          )
    w.generate(txt)
    w.to_file("wordcloud.png")
