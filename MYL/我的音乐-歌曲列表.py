from selenium import webdriver
import re
import csv
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import requests


# 在图中正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#提取歌名 去掉末尾的换行符
def cleanSongname(contents):
	datas = re.findall("(.*?)\n", contents, re.S)
	content = ""
	i = 0
	for data in datas:
		i += 1
		if i % 2 != 0:
			content += data
	return content

#提取歌手名	去掉末尾的换行符
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

	#找到我喜欢的音乐歌单网址
	def getUrl(self):
		# 打开网址
		self.driver.get(self.url)
		# 进入内嵌html
		iframe_element = self.driver.find_element_by_id("g_iframe")
		self.driver.switch_to.frame(iframe_element)
		#网页源代码
		text = self.driver.page_source
		ac_url="https://music.163.com/#"
		urls=re.findall(r'.*?class="tit f-thide s-fc0" href="(.*?)" ', text)
		ac_url=ac_url+urls[0]
		return ac_url

	def getContent(self):
		# 打开网址
		self.driver.get(self.url)
		# 进入内嵌html
		iframe_element = self.driver.find_element_by_id("g_iframe")
		self.driver.switch_to.frame(iframe_element)

		names = []
		with open("我喜欢的音乐.csv", "w", newline='', encoding='utf-8-sig') as f:
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
					# 写入csv文件
					csv_writer.writerow([song_name, hunmen_name])
			except:
				print("爬取结束!")
		f.close()
		self.driver.close()

	#绘图
	def Draw(self):
		for name in self.names:
			if self.names.count(name) > 0:
				self.count[name] = self.names.count(name)
		#按歌手出现的次数由大到小排序
		self.count = sorted(self.count.items(), key=lambda x: x[1], reverse=True)
		x = []
		y = []

		#取次数最多的前十位歌手
		temp1 = 0
		f1 = open("歌手.txt", "w", encoding='utf-8')
		if len(self.count) > 10:
			for i in self.count:
				if temp1 < 10:
					x.append(i[0])
					y.append(i[1])
				temp1 += 1
				f1.write(i[0])
				f1.write("\n")
		else:
			for i in self.count:
				x.append(i[0])
				y.append(i[1])
				f1.write(i[0])
				f1.write("\n")

		# 柱状图
		plt.figure()
		plt.bar(range(len(y)), y, tick_label=x)
		plt.xticks(rotation=30)			#倾斜横坐标
		plt.savefig("柱状图.png")
		plt.show()

		# 饼状图
		plt.figure()
		plt.pie(y, labels=x, autopct="%1.1f%%", shadow=False, startangle=50)
		plt.axis('equal')
		plt.savefig("饼状图.png")
		plt.show()

	#绘制词云
	def WC(self):
		with open("歌手.txt",encoding='utf-8') as fp:
			text = fp.read()
			font = r'C:\Windows\Fonts\simfang.ttf'
			wordcloud = WordCloud(background_color='white',font_path=font, width=1400, height=1400).generate(text)
			wordcloud.to_file("词云.jpg")
			plt.imshow(wordcloud)
			plt.show()

if __name__ == '__main__':
	hun_url=input("请输入用户的网易云音乐网址：")
	#hun_url="https://music.163.com/#/user/home?id=78940979"
	WYY1 = WangYiYun(hun_url)
	url = WYY1.getUrl()
	print("用户喜欢的音乐网址："+url)

	WYY2 = WangYiYun(url)
	WYY2.getContent()
	WYY2.Draw()
	WYY2.WC()