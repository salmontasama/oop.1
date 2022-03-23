num_ = 1000
print(num_.__dir__())
print(num_.bit_length())

class Studant:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name+" "+str(self.age)

student1=Studant('salmon',24)
student2=Studant('daniel',28)
print(student2)
print(student1)

class Car:
    def __init__(self,wheels,model,year,price):
        self.__wheels=wheels
        self.__model=model
        self.__year=year
        self.__price=price
        if wheels <4:
            print('impossble')
            self.wheels = 4

    def getWheels(self):
        return self.__wheels
    def setWheels(self, wheels):
        self.__wheels = wheels
    def getModel(self):
        return self.__model
    def setModel(self,model):
        self.__model=model
    def getYear(self):
        return self.__year
    def setModel(self,__year):
        self.__year=year
    def getPrice(self):
        return self.__price
    def setPrice(self,__year):
        self.__price=year
    def __str__(self):
        return str(self.__wheels,self.__model,self.__year,self.__price)


car1=Car(5,82,98,2500)
car2=Car(4,87,98,8222)
car3=Car(4,65,87,9000)

print(car1.getWheels())
car1.setWheels(4)
print('New',car1.getWheels())

class Circle:
    def __init__(self,area=25,color='blue'):
        self.__area=area
        self.__color=color
    def setArea(self,area):
        self.__area
    def getArea(self):
        return self.__area
    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color
    def __str__(self):
        return str(self.__area)+" "+self.__color
c1=Circle()
print(c1)
c2=Circle(32,'green')
print(c2)
print(c1.getArea())