import random
import math

# global object to be tossed around and edited easily
yourRoll = []
picturedRoll = []
# class for the methods of the Dice
class Dice:
    def __init__(sides, count):
        sides.count = count

    # calculates random number, multiplies by number of sides, then rounds up to max number. max random number does not exceed 6
    def roll(x):
        return(math.ceil(x * random.random()))

    # unsure what was asked of the material as it seems redundant 
    def getCurrentFaceValue(x):
        return(x)
    
    # Extra credit assigning emojis to dice face number using a for loop. 
    def showDiceFace(x):
        for x in range(0,len(yourRoll)):
            global picturedRoll
            if yourRoll[x] == 1:
                picturedRoll.append('⚀')
            elif yourRoll[x] == 2: 
                picturedRoll.append('⚁')
            elif yourRoll[x] == 3: 
                picturedRoll.append('⚂')
            elif yourRoll[x] == 4: 
                picturedRoll.append('⚃')
            elif yourRoll[x] == 5: 
                picturedRoll.append('⚄')
            elif yourRoll[x] == 6: 
                picturedRoll.append('⚅')
        print(picturedRoll)


def rollDice():
    # used a for loop to iterate through 5 times
    for x in range(5):
        testDice = Dice(6)
        roll = Dice.roll(testDice.count)
        value = Dice.getCurrentFaceValue(roll)
        global yourRoll
        yourRoll.append(int(value))
    Dice.showDiceFace(yourRoll)
    # YOU CAN USE THIS IS YOU CANT GET A YAHTZEE ROLL
    # yourRoll = [1,1,1,1,1]
    result = all(element == yourRoll[0] for element in yourRoll)
    if (result):
        print('YAHTZEE')
    
# HIT IT!
rollDice()

