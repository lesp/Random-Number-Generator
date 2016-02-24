from random import randint
from random import shuffle
from time import sleep

def rng(end,winners):
    numbers = []
    for number in range(end):
        numbers.append(int(number))
    shuffle(numbers)
    for winner in range(0,winners):
        print("The winners are: ",numbers[winner])
        
