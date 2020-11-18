#map and 2 list 1
li=[1,2,3,4,5,6,7,8,9,10]
mi=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
def func(x):
    return x**x

print([func(x) for x in li and mi])
print(list(map(func,li and mi)))
