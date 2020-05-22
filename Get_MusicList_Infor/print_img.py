#绘图文件
import matplotlib.pyplot as plt
from PIL import Image

#结构化程序设计

'''数据部分——网易云标签分类'''
language = ['华语','欧美','日语','韩语','粤语']
style = ['流行', '摇滚', '民谣', '电子', '舞曲', '说唱', '轻音乐', '爵士', '乡村', 'R&B/Soul', '古典', '民族', '英伦', '金属', '朋克', '蓝调', '雷鬼', '世界音乐', '拉丁', 'New Age', '古风', '后摇', 'Bossa Nova']
scene = ['清晨', '夜晚', '学习', '工作', '午休', '下午茶', '地铁', '驾车', '运动', '旅行', '散步', '酒吧']
emotion = ['怀旧', '清新', '浪漫', '伤感', '治愈', '放松', '孤独', '感动', '兴奋', '快乐', '安静', '思念']
theme = ['综艺', '影视原声', 'ACG', '儿童', '校园', '游戏', '70后', '80后', '90后', '网络歌曲', 'KTV', '经典', '翻唱', '吉他', '钢琴', '器乐', '榜单', '00后']

def print1(names,nums):
	'''散点图''' 
	plt.plot(names,nums,'o',markersize = 2)
	plt.xticks(fontproperties = 'SimHei', size = 5,rotation=45)
	#plt.show()
	plt.savefig('page1',dpi = 600)#保存图像
	plt.clf()#清空画布

def print2(names,nums):
	'''折线图'''
	plt.plot(names,nums,'r+-',markersize = 5)
	plt.xticks(fontproperties = 'SimHei', size = 5,rotation=45)
	#plt.show()
	plt.savefig('page2',dpi = 600)
	plt.clf()

def print3(names,nums,i):
	'''饼图'''
	types = {'fontproperties':'SimHei','fontsize':10}
	autopct = '%1.1f%%'
	explode = []
	for ele in nums:
		if ele == 22:
			explode.append(0.1)
		else:
			explode.append(0)

	plt.pie(nums,labels = names,autopct = autopct,textprops = types,explode = explode)
	#plt.show()
	plt.savefig('piepage'+str(i),dpi = 600)
	plt.clf()

def print4(names,nums,i):
	'''直方图'''
	plt.bar(names,nums,0.9,label = 'num',color = 'Teal')
	plt.xlabel = 'name'
	plt.ylabel = 'number'
	plt.xticks(fontproperties = 'SimHei', size = 5,rotation=45)
	plt.title = 'tag'
	plt.savefig('barpage'+str(i),dpi = 600)
	#plt.show()
	plt.clf()

def select(lists,dics):#筛选横纵轴的内容
	newdics = {}
	for words in lists:
		if words in dics:
			newdics[words] = dics[words]
	return newdics

def depart(list1):#元组分解为列表
	names,nums= zip(*list1)
	names = list(names)
	nums = list(nums) 
	return names,nums

def link(lists,tag = ''):#图片名集,类型名
	'''图片拼接'''
	toImage = Image.new('RGBA',(3840,8640))
	for i in range(len(lists)):
		fromImage = Image.open(lists[i])
		loc = (0,(i%3)*2880)
		toImage.paste(fromImage,loc)
		toImage.save(tag+'final.png')

def mixprint3(dics,dics0):
	'''三个饼图拼接'''
	lists = []
	i = 1;
	sdics = select(language,dics)
	list1 = sorted(sdics.items(),key = lambda x:x[1],reverse = True)
	names,nums = depart(list1)
	print3(names,nums,i)
	lists.append('piepage'+str(i)+'.png')
	
	i+= 1
	sdics = select(style,dics)
	list1 = sorted(sdics.items(),key = lambda x:x[1],reverse = True)
	names,nums = depart(list1)
	print3(names,nums,i)
	lists.append('piepage'+str(i)+'.png')

	i+= 1
	list1 = sorted(dics0.items(),key = lambda x:x[1],reverse = True)
	names,nums = depart(list1)
	print3(names,nums,i)
	lists.append('piepage'+str(i)+'.png')

	link(lists,'pie')


def mixprint4(dics,dics0):
	'''三个直方图拼接'''
	lists = []
	i = 1;
	sdics = select(language,dics)
	list1 = sorted(sdics.items(),key = lambda x:x[1],reverse = True)
	names,nums = depart(list1)
	print4(names,nums,i)
	lists.append('barpage'+str(i)+'.png')
	
	i+= 1
	sdics = select(style,dics)
	list1 = sorted(sdics.items(),key = lambda x:x[1],reverse = True)
	names,nums = depart(list1)
	print4(names,nums,i)
	lists.append('barpage'+str(i)+'.png')

	i+= 1
	list1 = sorted(dics0.items(),key = lambda x:x[1],reverse = True)
	names,nums = depart(list1)
	print4(names,nums,i)
	lists.append('barpage'+str(i)+'.png')

	link(lists,'bar')
