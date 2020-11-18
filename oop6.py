
def func(x):
    func2=lambda x: x+15
    return func2(x)+80
func3=lambda x,y : (x+y)*10
print(func(5))
print(func3(5,5))

