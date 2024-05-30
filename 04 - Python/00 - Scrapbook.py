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

class seconds_in_Time:
    info = "seconds in minute, hour, day, year"
    def __init__(seconds, timeRange):
        
    
        seconds_in_minute = float(60)
        seconds_in_hour = seconds_in_minute * 60
        seconds_in_day = seconds_in_hour * 24
        seconds_in_year = seconds_in_day * 365
