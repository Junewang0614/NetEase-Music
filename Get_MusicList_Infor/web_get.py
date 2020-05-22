from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

class Tag():#用于保存计数好的标签
	'''标签类'''
	def __init__(self,dic = {}):
		self.dic = dic #完整标签字典，用于分类统计用
		self.dic0 = {'其他':0} #不完整标签字典，用于简化汇总用

	def reset(self):
		'''用于再次将数据整理'''
		'''标签数小于等于2的归类为其他'''
		for key,value in self.dic.items():
			if value <= 2:
				self.dic0['其他'] += value
			else:
				self.dic0[key] = value


class Data():#数据类，爬取相关内容并保存
	
	def __init__(self,url,browser):
		self.url = url
		self.browser = browser
		self.cbox = [] #用户创建歌单
		self.sbox = [] #用户收藏歌单
		self.tags = Tag() #用户歌单的标签及数据

	def write_data_csv(self,filename,lists):
		'''名称写入csv文件,方便用户查看'''
		with open(filename+'.csv','w',encoding = 'utf-8-sig',newline = '') as f:
			i = 1;
			writer = csv.writer(f)
			writer.writerow([str(filename)])
			for ment in lists:
				writer.writerow([str(i),ment.get_attribute('title')])
				i+= 1;
			f.close()

	def write_data_txt(self,filename,lists):
		'''名称写入txt文件，方便后续处理'''
		with open(filename+'.txt','w',encoding = 'utf-8') as f:
			for ments in lists:
				f.write(ments.get_attribute('title')+'\n')

	def getin_pages(self):
		#进入网页爬取信息
		'''数据部分'''
		id0 ='g_iframe'
		per = 10 #用于向下滚动页面加载

		'''操作部分'''
		#模拟访问操作
		self.browser.get(self.url)
		self.browser.switch_to.frame(id0)#进入需要访问的内页
		#模拟鼠标向下滚动加载
		for i in range(per):
			self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
			sleep(2)#每个页面两秒时间加载

	def get_cbox(self):
		'''获取用户创建的歌单并写入文件'''
		self.cbox = self.browser.find_elements_by_css_selector('#cBox li a[class = "tit f-thide s-fc0"]')
		filename = '用户创建的歌单列表'
		self.write_data_csv(filename,self.cbox)
		self.write_data_txt(filename,self.cbox)

	def get_sbox(self):
		'''获取用户收藏的歌单并写入文件'''
		self.sbox = self.browser.find_elements_by_css_selector('#sBox li a[class = "tit f-thide s-fc0"]')
		filename = '用户收藏的歌单列表'
		self.write_data_csv(filename,self.sbox)
		self.write_data_txt(filename,self.sbox)

	def get_moreinfo(self):
		'''获取与歌单更详细的信息内容'''
		id0 ='g_iframe'
		#i = 0
		s_news = []#收藏歌单的子页面的url
		for li in self.sbox:#需要另保存在一个列表里，因为会存在过时问题
			newurl = str(li.get_attribute('href'))#这是歌单的网址
			s_news.append(newurl)
		for li in s_news:
			self.browser.get(li)
			self.browser.switch_to.frame(id0)
			self.get_tags()
			self.get_desc()
			#i+=1

	def get_tags(self):
		'''获取用户创建和收藏歌单的标签'''
		with open("tag.txt","a",encoding = 'utf-8') as f:
			try:
				lis = self.browser.find_elements_by_css_selector('.u-tag i')
			except NoSuchElementException:
				pass
			else:
				for li in lis:
					text = li.text.strip('\n')#删掉换行符
					#self.tags.append(text)
					if text in self.tags.dic:
						self.tags.dic[text] += 1
					else:
						self.tags.dic[text] = 1
					f.write(li.text+'\n')

	def get_desc(self):
		'''获取用户创建和收藏歌单的简介'''
		with open('desc.txt','a',encoding = 'utf-8') as f:
			#判断内容是否需要展开
			try:
				check = self.browser.find_element_by_css_selector('#album-desc-spread')
			except NoSuchElementException:
				pass
			else:
				self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
				#browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')#防止按钮覆盖问题
				if check.text.endswith('展开'):
						check.click()
						#sleep(2)
			#判断是否有简介信息
			try: 
				des = self.browser.find_element_by_css_selector('#album-desc-more')
			except NoSuchElementException:
				pass
			else:
				f.write(des.text+'\n\n')


def get_infor():
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')

	url = input('请输入用户的网易云音乐主页网址：')
	browser = webdriver.Chrome(options = chrome_options)#使用谷歌浏览器
	data = Data(url,browser)
	data.getin_pages()
	data.get_cbox()
	data.get_sbox()
	data.get_moreinfo()
	print('over')
	browser.close()

	return data

def main():
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')
	url = input('请输入用户的网易云音乐主页网址：')
	browser = webdriver.Chrome(options = chrome_options)#使用谷歌浏览器
	data = Data(url,browser)
	data.getin_pages()
	data.get_cbox()
	data.get_sbox()
	data.get_moreinfo()
	print('over')
	for key,values in data.tags.dic.items():
		print(str(key)+":"+str(values))
	browser.close()

if __name__ == '__main__':
	'''不弹出页面进行网页爬虫'''
	main()