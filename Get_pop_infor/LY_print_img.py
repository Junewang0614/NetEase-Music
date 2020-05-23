import matplotlib.pyplot as plt  

def popsong():  
    name_list = ['Chinese','English','The other']  
    num_list = [92,6,2]  
    plt.bar(range(len(num_list)), num_list,color='rgb',tick_label=name_list)  
    plt.show()  

def popsinger():
    name_list = ['Chinese','English','The other']  
    num_list = [92,6,2]  
    plt.bar(range(len(num_list)), num_list,color='rgb',tick_label=name_list)  
    plt.show()
    
if __name__=="__main__":
    popsong()
    popsinger()
