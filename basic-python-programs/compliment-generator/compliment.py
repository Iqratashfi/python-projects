import random

name = input("heyyy! Tell me your name ")
compliments = ["You are sooo amazing",
               "You are sooo great",
               "You are a little star",
               "You can do it"
               "You are the BEST",
               "You have a beautiful smile",
               "You are adorable"]

num = int(input(name+ " How many compliments do u need today?"))
print("Here you go\n")

for _ in range(num):
    print(name+ "," +random.choice(compliments))
