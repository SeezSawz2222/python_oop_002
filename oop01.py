class Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak (self):
        print('Hi I am ',self.name,'& I am ',self.age,'years old')
    def chng_age(self,age):
        self.age=age
    def weight(self,weight):
        self.weight=weight
        print(self.name,"weights  ",self.weight,'KG')
        

Santo=Dog('Santo',23)
ridoy=Dog('Ridoy',23)
Santo.chng_age(22)
Santo.speak()
ridoy.speak()
Santo.weight(76)

