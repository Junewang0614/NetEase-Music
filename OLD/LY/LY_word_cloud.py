from wordcloud import WordCloud
import matplotlib.pyplot as plt  #绘制图像的模块

def popsong():
    path_txt=r'C:\Users\lenovo\Desktop\popsong.txt'
    f = open(path_txt,'r',encoding='UTF-8').read()


    wordcloud = WordCloud(
       #设置字体
       font_path="C:/Windows/Fonts/simfang.ttf",
       #设置背景，宽高
       background_color="white",width=1000,height=880).generate(f)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def popsinger():
    path1_txt=r'C:\Users\lenovo\Desktop\popsinger.txt'
    f1 = open(path1_txt,'r',encoding='UTF-8').read()


    wordcloud = WordCloud(
       #设置字体
       font_path="C:/Windows/Fonts/simfang.ttf",
       #设置背景，宽高
       background_color="white",width=1000,height=880).generate(f1)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    
if __name__=="__main__":
    popsong()
    popsinger() 
