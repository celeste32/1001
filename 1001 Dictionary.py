#字典 Dictionary
a = {'Mercury':'水星','Venus':'金星','Earth':'地球','Mars':'火星'}
     #key      #value
print(a['Mercury']) #遍訪所有值
for key in a.keys():
    print('key:{},value:{}'.format(key,a[key]))
    print(f'key:{key},value:{a[key]}')
a['Earth']='地獄'
for key in a.keys():
    print('key:{},value:{}'.format(key,a[key])) #地球會被地獄覆寫過去
a.pop('Venus')
for key in a.keys():
    print(key,a[key])
#print(a['Saturn']) #錯誤發生時機 1.編譯時期錯誤 2.執行時期錯誤
print(a.get('Saturn','靠北啊沒這東西')) #抓Saturn抓不到  直接跳第二句出來
try:
    print(a['Saturn'])
except:
    print('沒這東西')
try:
    print(a['Saturn'])
except Exception as e:
    print('沒這東西')
    print(e)

tea = []
d = {'id':1,'商品':'烏龍茶','單價':150}
tea.append(d)
d = {'id':2,'商品':'鐵觀音','單價':200}
tea.append(d)
d = {'id':3,'商品':'普洱茶','單價':300}
tea.append(d)
for l in tea:
    print(l['商品'])
a = [['a','b','c'],['d','e','f']]
print(a[0][1]) #取a中第0個list再取第1個索引
import numpy as np
import random
n = 100
d = np.zeros([n])
for i in range(n):
    d[i] = random.randint(1,100)
    def sort(d): #def sort()自訂函數
        sort(d) #NameError
        print(d)
#氣泡排序法
def sort(d):
    for i in range(len(d)-2+1):
        for j in range(i+1,len(d)-1+1):
            if d[i]>d[j]:
                tmp=d[i]
                d[i]=d[j]
                d[j]=tmp

