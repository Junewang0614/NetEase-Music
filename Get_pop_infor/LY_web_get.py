import requests
from bs4 import BeautifulSoup
import json  

def popsong():
    headers={
        'Host':'music.163.com',
        'Referer':'http://music.163.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
        }

    url='http://music.163.com/discover/toplist'
    r=requests.session()
    r=BeautifulSoup(r.get(url,headers=headers).content)
    result=r.find('ul',{'class':'f-hide'}).find_all('a')
#print(reslut)
 
    music=[]  #用于接受返回值
    i=1
    for mu in result:
    #print('{}:{}'.format(music.text,music['href']))
        c='No.{}:{}'.format(i,mu.text)
        i=i+1
        music.append(c)
    
    music[1]
    from pprint import pprint  #格式化输出
    pprint(music)


def popsinger():  
    a_headers = {"Referer": "http://music.163.com/discover/artist"  }
          #对付防盗链，服务器会识别headers中的referer是不是它自己，如果不是，有的服务器不会响应，所以我们还可以在headers中加入referer
    url="http://music.163.com/weapi/artist/top?csrf_token="    #在开发者选项找到热门歌手对应的url，请求方式为post
    data={"params":"uAE0hN7yRCy+plWTUJw7imQQW+wUSFRuVlFD8UTgXNfJTVLzNyqfnLRqSByCjs40san8rbwMfpasdpJRNit6vKkbQE0F7MZEgRPgSEVfXrHIB/wGiyYQ/VIaZnyTql1m",  
          "encSecKey":"def9762a8c6ff1f3ae1a7ee23cbc095b3dd6c888f28e974ca00f927fd044a48cfdde49af3138aa99fa7da17fdb97809c7d1abd4ddfc40ab7ef3c0e574e56b2d623c0c23af4d08c629087fd5e1996c961af133140dc81b9fb2322aca668a8079c6cd01a0699fc860b2bb0df47b3887d563f1b18e6585198bb5d9c718a5fa92f04"}  
    #用Requests和urlopen解析歌手页面的POST  
    req=requests.post(url=url,headers=a_headers,data=data)  #利用Request将headers，dict，data整合成一个对象传入urlopen
    #Request存在的意义是便于在请求的时候传入一些信息，而urlopen则不
    req.encoding="utf-8"   
    #解析所返回的JSON数据  
    a_data=json.loads(req.text)  #字典，含code,more,artist，其中artist是列表，含歌手名字与ID
    a_list=a_data["artists"]#刚刚观察返回数据可以知道歌手的信息储存在artists键中  
    id_list=[]#用一个列表储存所有歌手的id和name  
    for i in range(len(a_list)):  
        a_dict = {}#用一个字典储存一个歌手的id和name  
        a_dict["name"]=a_list[i]["name"]
        id_list.append(a_dict)  
    return id_list  
 
if __name__=="__main__":
    popsong()
    print(popsinger()) 
