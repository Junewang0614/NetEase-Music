#绘图文件
import matplotlib.pyplot as plt
#数据
from countnew import names,nums

'''散点图''' 
plt.plot(names,nums,'o',markersize = 2)
plt.xticks(fontproperties = 'SimHei', size = 5,rotation=45)
#plt.show()
plt.savefig('page1',dpi = 600)#保存图像
plt.clf()#清空画布

'''折线图'''
plt.plot(names,nums,'r+-',markersize = 5)
plt.xticks(fontproperties = 'SimHei', size = 5,rotation=45)
#plt.show()
plt.savefig('page2',dpi = 600)
plt.clf()

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
plt.savefig('page3',dpi = 600)
plt.close()