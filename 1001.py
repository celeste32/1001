#陣列型態
import numpy as np
a = np.array([1,2,3],dtype = np.int64)
print(a.dtype) #int32
b = np.array([1.0,2.0,3.0],dtype = np.int32)
print(b.dtype) #float 64
print(b)
c = np.array([1,2,3],dtype='int64')
print(c.dtype)
d = np.int32([1,2,3])
print(d.dtype)

#slicing 切片
a = np.int32([1,2,3,4,5,6,7,8,9,10])
             #0 1 2 3 4 5 6 7 8 9
print(a[3:5]) #從索引3開始取得，到索引5結束，但不包含5
print(a[3:-1]) #[-1]取最後一位的值
