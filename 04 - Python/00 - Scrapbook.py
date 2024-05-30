import random

class Dog:
    infoVariable = "some information about a mammal goes here"
    def __init__(self, name):
        print("I'm alive!")
        self.luckyNumber = (random.randint(1,10))
        self.name = name

    def bark(self):
        print(f"Bark. I am {self.name}! Favorite Number is {self.luckyNumber}.")


dog1 = Dog("Fido")
dog2 = Dog("Sara")
dog1.bark()
dog2.bark() 


class Notebook:
    info = "pad of paper, lightly scribbled"
    def __init__(self, name):
        print("I am a notebook!")
        self.luckyNumber = (random.randint(100,1000))
        self.name = name

notebook1 = Notebook("NB1")
notebook2 = Notebook("NB2")

