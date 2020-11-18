#Counter, subtract,update,clear,union, &, | 
import collections
from collections import Counter
c=Counter('SSSSAAANNTTOOO')
print(c)
d=Counter([111,1,1,1,1,1,2,2,22,2,2,3,3,33,44,4,4,45,5,5,5,6,67,7,7,7,7,8,8,8,89,9,9])
print(d)
print(d.most_common(3))
e=Counter(a=4,b=4,c=3,d=3,e=2)
d=['a','b','c','c','d','e']
e.subtract(d)
print(e)
e.update(d)
e.clear()
print(e)
c=Counter(a=4,b=2,c=0,d=-2)
d=Counter(['a','b','c','b'])
print(c | d)
print(c & d)

