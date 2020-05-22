import wordcloud
import jieba
import imageio

#分词与构造词云
#绘制三个词云：标签词云、标题词云、简介词云
#以此提取听歌关键词
class Cloud():
	def __init__(self,mk,txt = ''):
		self.txt = txt
		self.pic = mk
		self.cloud = wordcloud.WordCloud(background_color = 'white',
						font_path = 'C:/Windows/Fonts/方正启体简体.ttf',
						mask = self.pic, 
						scale = 15,
						max_words = 120,
						stopwords = {'介绍','一个','我们','你们','自己','这些','一些','可以','一首','不要','不是','这个'})

	def read_txt(self,filename):
		'''读取制作词云的文本'''
		with open(filename,'r',encoding = 'utf-8') as f:
			self.txt += f.read()
		self.txt = self.txt.replace('\n',' ')

	def depart(self,filename):
		'''将文本分词后生成制作词云文本'''
		with open(filename,'r',encoding = 'utf-8') as f:
			txt = f.read()
		words = jieba.lcut(txt)
		self.txt += ' '.join(words)

	def make(self,filename):
		'''制作词云'''
		self.cloud.generate(self.txt)
		self.cloud.to_file(filename)
	
	def clear_txt(self):
		'''清空内容'''
		self.txt = ''
		

def makeclouds():
#def main():
	mk = imageio.imread('3.jpg')
	ofilename = 'tag.txt'
	nfilename = 'tag.png'
	cloud = Cloud(mk = mk)
	cloud.read_txt(ofilename)
	cloud.make(nfilename)

	mk = imageio.imread('4.jpg')
	cloud = Cloud(mk = mk)
	ofilename = '用户创建的歌单列表.txt'
	nfilename = 'name.png'
	cloud.depart(ofilename)
	ofilename = '用户收藏的歌单列表.txt'
	cloud.depart(ofilename)
	cloud.make(nfilename)

	mk = imageio.imread('1.jpg')
	cloud = Cloud(mk = mk)
	ofilename = 'desc.txt'
	nfilename = 'desc.png'
	cloud.depart(ofilename)
	cloud.make(nfilename)

if __name__ == '__main__':
	main()

