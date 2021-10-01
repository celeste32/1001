import numpy as np
import random
from CelesteSDK import sort
from CelesteSDK import area
n = 10
d = np.zeros([n])
for i in range(n):
    d[i] = random.randint(1,100)
sort(d)
print(d)
a = area(10)
print(a)