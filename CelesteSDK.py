#把此檔編譯成二進位檔
import numpy as np
def sort(d):
    for i in range(len(d)-2+1):
        for j in range(i+1,len(d)-1+1):
            if d[i]>d[j]:
                tmp=d[i]
                d[i]=d[j]
                d[j]=tmp
def sort(d):
    pass
def area(r):
    return np.pi*r*r