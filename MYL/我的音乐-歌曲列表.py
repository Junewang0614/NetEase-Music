from selenium import webdriver
import csv
import time
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import PIL.Image as image


# 在图中正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def cleanSongname(contents):
	datas = re.findall("(.*?)\n", contents, re.S)
	content = ""
	i = 0
	for data in datas:
		i += 1
		if i % 2 != 0:
			content += data
	return content


def cleanHunmanname(contents):
	datas = re.findall("(.*?)\n", contents, re.S)
	content = ""
	for data in datas:
		content += data
	return content


class WangYiYun(object):
	def __init__(self, url):
		self.url = url
		self.names = []
		self.count = {}
		self.driver = webdriver.Firefox()

	def cleanContent(self, content):
		datas = re.findall("(.*?)\n(.*?)", content, re.S)
		print(datas)

	def getContent(self):
		# 打开网址
		self.driver.get(self.url)
		# 进入内嵌html
		iframe_element = self.driver.find_element_by_id("g_iframe")
		self.driver.switch_to.frame(iframe_element)

		names = []
		with open("我喜欢的音乐.csv", "w", newline='', encoding='utf-8') as f:
			csv_writer = csv.writer(f)
			csv_writer.writerow(['歌名', '歌手'])
			try:
				for i in range(1, 1000):
					# 找歌名
					songs = self.driver.find_element_by_xpath(str.format('//tbody/tr[{0}]/td[2]', i))
					song_name = songs.find_element_by_css_selector('a[href^="/song?id="]').text
					song_name = song_name + '\n'
					song_name = cleanSongname(song_name)
					print("歌名:" + song_name)
					# 找作者
					hunmen = self.driver.find_element_by_xpath(str.format('//tbody/tr[{0}]/td[4]', i))
					hunmen_name = hunmen.find_element_by_css_selector('a[class=""]').text
					hunmen_name = hunmen_name + '\n'
					hunmen_name = cleanHunmanname(hunmen_name)
					print("作者:"+hunmen_name)
					self.names.append(hunmen_name)
					# 写入文件
					csv_writer.writerow([song_name, hunmen_name])
			except:
				print("断掉了!")
		f.close()
		self.driver.close()

	def Draw(self):
		for name in self.names:
			if self.names.count(name) > 0:
				self.count[name] = self.names.count(name)
		self.count = sorted(self.count.items(), key=lambda x: x[1], reverse=True)
		#print(self.count)
		x = []
		y = []
		temp1 = 0
		temp2 = 0
		f1 = open("歌手.txt", "w", encoding='utf-8')
		if len(self.count) > 10:
			for i in self.count:
				if temp1 < 10:
					x.append(i[0])
					y.append(i[1])
				else:
					temp2 += i[1]
				temp1 += 1
				f1.write(i[0])
				f1.write("\n")
			x.append("其他")
			y.append(temp2)
		else:
			for i in self.count:
				x.append(i[0])
				y.append(i[1])
				f1.write(i[0])
				f1.write("\n")

		#print(x)
		#print(y)

		# 柱状图
		plt.figure()
		plt.bar(range(len(y)), y, tick_label=x)
		plt.show()
		# 饼状图
		plt.figure()
		plt.pie(y, labels=x, autopct="%1.1f%%", shadow=False, startangle=50)
		plt.axis('equal')
		plt.show()

	def WC(self):
		with open("歌手.txt",encoding='utf-8') as fp:
			text = fp.read()
			print(text)
			font = r'C:\Windows\Fonts\simfang.ttf'
			wordcloud = WordCloud(background_color='white',font_path=font, width=1400, height=1400).generate(text)
			wordcloud.to_file("词云.jpg")
			plt.imshow(wordcloud)
			plt.show()

if __name__ == '__main__':
	url = 'https://music.163.com/#/playlist?id=726768097'
	WYY = WangYiYun(url)
	WYY.getContent()
	WYY.Draw()
	WYY.WC()