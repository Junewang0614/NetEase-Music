import web_get as ng#用于爬虫
import print_img as pi #用于生成数据表
import word_cloud as wc #用于生成词云

#数据获取
def main():
	'''爬虫爬取内容'''
	data = ng.get_infor()
	data.tags.reset()
	'''生成图表'''
	pi.mixprint3(data.tags.dic,data.tags.dic0)
	pi.mixprint4(data.tags.dic,data.tags.dic0)
	'''生成词云'''
	wc.makeclouds()

if __name__ == '__main__':
	main()




