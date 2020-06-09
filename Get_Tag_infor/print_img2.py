import matplotlib.pyplot as plt
import jieba

def print():
    f = open("result1.txt", 'r', encoding='utf-8').read()
    counts = {}
    wordsList =jieba.lcut(f)
    for word in wordsList:
        word = word.replace("，", "").replace("！", "").replace("“", "") \
            .replace("”", "").replace("。", "").replace("？", "").replace("：", "") \
            .replace("...", "").replace("、", "").strip(' ').strip('\r\n')
        if len(word) == 1 or word == "":
            continue
        else:
            counts[word]=counts.get(word,0)+1 #单词计数
    list1=sorted(counts.items(),key=lambda x:x[1],reverse=True)
    items = list(counts.items()) #将字典转为list
    items.sort(key=lambda x:x[1],reverse=True) #根据单词出现次数降序排序
    names,nums = zip(*list1)#此时是元组
    names = list(names)
    nums = list(nums)
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
