from selenium import webdriver
import csv
import time
import re


def cleanSongname(contents):
    datas = re.findall("(.*?)\n", contents, re.S)
    content=""
    i=0
    for data in datas:
        i+=1
        if i%2!=0:
            content+=data
    return content

def cleanHunmanname(contents):
    datas = re.findall("(.*?)\n", contents, re.S)
    content=""
    for data in datas:
        content+=data
    return content

class WangYiYun(object):
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()

    def cleanContent(self, content):
        datas=re.findall("(.*?)\n(.*?)", content, re.S)
        print(datas)

    def getContent(self):
        # 打开网址
        self.driver.get(self.url)
        # 进入内嵌html
        iframe_element = self.driver.find_element_by_id("g_iframe")
        self.driver.switch_to.frame(iframe_element)

        with open("我喜欢的音乐.csv", "w", newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['歌名','歌手'])
            try:
                for i in range(400, 1000):
                    #找歌名
                    songs = self.driver.find_element_by_xpath(str.format('//tbody/tr[{0}]/td[2]', i))
                    #songs = self.driver.find_element_by_xpath('//tbody/tr[640]')
                    song_name = songs.find_element_by_css_selector('a[href^="/song?id="]').text
                    song_name = song_name + '\n'
                    song_name = cleanSongname(song_name)
                    print("歌名:" + song_name)

                    #找作者
                    hunmen = self.driver.find_element_by_xpath(str.format('//tbody/tr[{0}]/td[4]', i))
                    hunmen_name = hunmen.find_element_by_css_selector('a[class=""]').text
                    hunmen_name = hunmen_name + '\n'
                    hunmen_name = cleanHunmanname(hunmen_name)
                    print("作者:"+hunmen_name)
                    print()

                    #写入文件
                    csv_writer.writerow([song_name, hunmen_name])
            except:
                pass
        f.close()
        self.driver.close()


if __name__ == '__main__':
    url = 'https://music.163.com/#/playlist?id=726768097'
    WYY = WangYiYun(url)
    WYY.getContent()