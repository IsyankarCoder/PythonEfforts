import numpy

deger = [10,23,30]
deger_dizi= numpy.array(deger,dtype=numpy.float)
print(deger_dizi)

deger_dizi2 = numpy.array([12,213,30],dtype=numpy.float)
print(deger_dizi2)

ort= (deger_dizi2+deger_dizi)/2
print(ort)


ikiboyutdizi = numpy.array([[1,23,4,5,6],[12,5,2,2,3]])
print(ikiboyutdizi)

x= numpy.array([25,45,14,66,81,93])
print(x[1:2])