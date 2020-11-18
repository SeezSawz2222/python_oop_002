class person(object):
    population=50

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def getpopulation(cls):
        return cls.population

    @staticmethod
    def isadult(age=17):
        return  age>=18

    def display(self):
        print(self.name, 'is',self.age,'years old')

new=person('Santo',22)
print(new.getpopulation())
print(new.isadult(12))
print(new.display())
