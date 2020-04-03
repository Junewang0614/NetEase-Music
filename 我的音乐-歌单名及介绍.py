from selenium import webdriver
import time
import pprint
import csv


class WangYiYun(object):
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()

    def getContent(self):
        # 打开网址
        self.driver.get(self.url)
        # 进入内嵌html
        iframe_elemnt = self.driver.find_element_by_id("g_iframe")
        self.driver.switch_to.frame(iframe_elemnt)

        with open("歌单名.csv", "w", newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['名称'])
            for i in range(1, 10):
                songs = self.driver.find_element_by_xpath(str.format('//ul[@class="f-cb j-flag"]/li[{0}]', i))
                print(songs)
                song_name = songs.find_element_by_css_selector('a[class="tit f-thide s-fc0"]').text
                print(song_name)
                csv_writer.writerow([song_name])
        f.close()
        self.driver.close()


if __name__ == '__main__':
    url = 'https://music.163.com/#/my/m/music/playlist?id=632590535'
    WYY = WangYiYun(url)
    WYY.getContent()
