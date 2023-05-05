class Cat:
    def __init__(self,name,feature,skin,say,type_animal):
        self.name = name
        self.feature = feature 
        self.skin = skin 
        self.say = say
# sử dụng hướng đối tượng xây con mèo nha Anh Lực
        self.type_animal = "Cat"
    pass

    def Say_something(self):
        print(f"{self.name} says 'Meow Meow'")
        pass

    def Ability(self):
        print(f"{self.name} can climb tree and fall on his/her feet")
        pass
# xây dựng trên các thuộc tính này nhan anh Lực deadline 5-5 nha anh

#Anh không rõ yêu cầu của em như thế nào nên là làm ba láp ba xàm nha
class Animal():
    def __init__(self,weight,color,name):
        self.name = name
        self.weight = weight
        self.color = color
    pass

    def Print_info(self):
        print (f"Name: {self.name}")
        print (f"Color: {self.color}")
        print(f"Weight: {self.weight}")
        pass

    def Say_something(self):
        print('Each animal makes different sound')
        pass

    def Ability(self):
        print('Animals have unique ability that disinguish themselves')
        pass

 class Cat(Animal):
    def __init__(self,weight,color,name):
        super().__init__(weight,color,name)
        self.type_animal = "Cat"
    pass

    def Say_something(self):
        print(f"{self.name} says 'Meow Meow'")
        pass

    def Ability(self):
        print(f"{self.name} can climb tree and fall on his/her feet")
        pass
