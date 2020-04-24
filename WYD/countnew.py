# 用于获得的文本数据处理

'''1、计数标签值'''
filename = 'tag_yll.txt'
dics = {} # 字典用于存标签和对应的数字
with open(filename,encoding = 'utf-8') as f:
	lines = f.readlines() #lines是将文件每一行都存成列表

for element in lines:
	element=element.strip('\n')#删除字符中的回车符s
	if element in dics:
		dics[element] += 1
	else:
		dics[element] = 1

#名称与数值的分离（用于做xy轴）
list1 = sorted(dics.items(),key = lambda x:x[1],reverse = True)
names,nums = zip(*list1)#此时是元组
names = list(names)
nums = list(nums)



