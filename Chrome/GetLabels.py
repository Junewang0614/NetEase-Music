import re
import urllib.request
import urllib.error
import urllib.parse  
import jieba
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get(url):
    links=[]
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    driver.switch_to.frame('g_iframe')  
    songs=driver.find_elements_by_xpath('//*[@id="sBox"]//li//a')#定位歌曲链接所在位置
    for song in songs:
        link1=song.get_attribute('href')#取出链接
        if link1=='javascript:;':
            continue;
        links.append(link1)
    return links

def get_Lables(url):
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    request = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')  # 打开url    
    html = str(html)  # 转换成str     
    w1='标签：'
    w2='，简介'
    pat = re.compile(w1+'(.*?)'+w2,re.S)#取出标签
    result = pat.findall(html)
    return result
    
f = open('result1.txt', 'a', encoding='utf-8')  # 写入文件
url="https://music.163.com/#/user/home?id=78940979"
links=get(url)
num=0
for j in links:        #遍历歌单
    label_=get_Lables(j)
    k=0
    if len(label_):
        f.write(label_[k])
        f.write('\n')
f.close()

f = open("result1.txt", 'r', encoding='utf-8').read()
f2 = open('result2.txt', 'a', encoding='utf-8')  # 写入文件
counts = {}
wordsList =jieba.lcut(f)
for word in wordsList:
    word = word.replace("，", "").replace("！", "").replace("“", "") \
        .replace("”", "").replace("。", "").replace("？", "").replace("：", "") \
        .replace("...", "").replace("、", "").strip(' ').strip('\r\n')
    if len(word) == 1 or word == "":
        continue
    else:
        counts[word]=counts.get(word,0)+1 #单词计数
items = list(counts.items()) #将字典转为list
items.sort(key=lambda x:x[1],reverse=True) #根据单词出现次数降序排序
    
for item in items:
    word,counter = item
    print("单词：{},次数：{}".format(word,counter))
    f2.write("单词：{},次数：{}".format(word,counter))
    f2.write('\n')
f2.close()
