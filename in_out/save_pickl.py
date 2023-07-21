"""
pickl的使用，将对象保存至特定的存储文件中，不可直观的查看

dump和dumps的区别：
dump是将对象序列化并保存至文件中
dumps是将对象序列化

load和loads的区别：
load是将序列化的对象从文件中读取并反序列化
loads是将序列化的对象反序列化
"""
import pickle as pkl

lst=[1,2]
with open ("./in_out/lst.pkl",'wb') as f:
    pkl.dump(lst,f)
    f.close()
with open("./in_out/lst.pkl",'rb') as f:
    lst=pkl.load(f)
    print(lst)
    f.close()
