import time
import random

name = input("Hello, what is your name? ")

time.sleep(1)
print("Hello " + name)

feeling = input("How are you today? ")

time.sleep(1)
if "good" in feeling:
    print("I'm feeling good too!")
else:
    print("I'm sorry to hear that!")

time.sleep(1)
favcolour = input("What is your favourite colour? ")

colours = ["Red","Green","Blue"]

time.sleep(1)
print("My favourite colour is " + random.choice(colours))

mood = input("What are you doing today? ")
mood = ["dancing", "reading", "playing", "watching TV", "hiking"]
time.sleep(1)
print("I feel like " + random.choice(mood) + " today")

love=input("Do you have a girlfriend? ")
love = ["Yes", "No"]
time.sleep(1)
input("cool")

food = input("Which food type do you like most? ")
food=["Asian", "Japanese", "Italian", "Chinese", "Latin"]
time.sleep(1)
print("I mostly like " + random.choice(food))

sport = input("Which sport do you love to watch the most? ")
sport=["cirket", "Baseball", "Soccer", "Rugby", "Athletics"]
time.sleep(1)
print("I love to watch " + random.choice(sport))
time.sleep(1)
print("I love talking with you!")


peak = input("Do you know the height of world's tallest mountain? ")
time.sleep(1)
print("8848")
print("Anyone can answer that.")

planet = input("How many planet are there in this solar system")
time.sleep(1)
print("I guess there are 8 planets")

horscope = input("What is the name of your horscope? ")
horscope=["Leo", "Cancer", "Capricon", "Pisces", "Virgo"]
time.sleep(1)
print("My horscope name is " + random.choice(horscope))

exe = input("How many sit up can you do? ")
exe=["15", "34", "25", "40", "50"]
time.sleep(1)
print("I can do around " + random.choice(exe))

tired = input("I am feeling tired today.")
time.sleep(1)
print("See you! Have a nice day.")







