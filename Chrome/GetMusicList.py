from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv

#写入文件,写入的都是当前lists里面的内容
def write_data(filename,lists):
	with open(filename+'.csv','w',encoding = 'utf-8-sig',newline = '') as f:
		i = 1;
		writer = csv.writer(f)
		writer.writerow([str(filename)])
		for ment in lists:
			writer.writerow([str(i),ment.get_attribute('title')])
			i+= 1;
		f.close()

#进入网页
def getin_pages(url):
	'''数据部分'''
	id0 ='g_iframe'
	per = 10 #用于向下滚动页面加载

	'''操作部分'''
	#模拟访问操作
	browser.get(url)
	browser.switch_to.frame(id0)#进入需要访问的内页
	#模拟鼠标向下滚动加载
	for i in range(per):
		browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
		sleep(2)#每个页面两秒时间加载

#获取用户创建的歌单并写入文件
def get_cbox():
	lists = []#新建空列表
	lists = browser.find_elements_by_css_selector('#cBox li a[class = "tit f-thide s-fc0"]')
	filename = '用户创建的歌单列表'
	write_data(filename,lists)

#获取用户收藏的歌单并写入文件
def get_sbox():
	lists = []#新建空列表
	lists = browser.find_elements_by_css_selector('#sBox li a[class = "tit f-thide s-fc0"]')
	filename = '用户收藏的歌单列表'
	write_data(filename,lists)

def main():
	url = input('请输入用户的网易云音乐主页网址：')
	getin_pages(url)
	get_cbox()
	get_sbox()


if __name__ == '__main__':
	'''不弹出页面进行网页爬虫'''
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')

	browser = webdriver.Chrome(options = chrome_options)#使用谷歌浏览器
	main()
	browser.close()
