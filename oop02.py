class Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak (self):
        print('Hi I am ',self.name,'& I am ',self.age,'years old')
    def talk(self):
        print('bark')


class Cat(Dog):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color
    def talk(self):
        print('Meow')
tim=Cat('Tim',4,'Black')
rad=Dog('San',6)
rad.speak()
tim.speak()
rad.talk()
tim.talk()
print(rad.age)

