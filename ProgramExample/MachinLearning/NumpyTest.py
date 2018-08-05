#_*_coding:utf-8_*_
import numpy as np
a = [1,2,3,4]
b = np.array(a)
#Öá
print b.ndim
#wei du;
print b.shape
print b.size
print b.dtype
print b.itemsize
print b.data

a = np.arange(15).reshape(3,5)
print a
print a.shape
print a.ndim
print a.dtype
print a.itemsize
print a.size
print type(a)

#create numpy's array from orginal array
a=np.array([2,3,4])
print a

print np.zeros((3,4))
print np.ones((2,3,4))
print np.empty((2,3))
print np.e