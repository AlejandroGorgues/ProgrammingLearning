import sys
import random
import math


#Function that initialize randomly the objects behind the door
def doorsPosition():
    doors = {}
    
    objects = ["Goat", "Goat", "Car"]

    for i in range (0,3):
        randomObject = random.randint(0,len(objects)-1)
        doors["%i" % i] = objects[randomObject]
        del objects[randomObject]
        
    return doors

#Process of selection by monty and by the contestant
def optionSelected(**doors):
    
    #Contestant door selection
    contestantSelection = random.randint(1,len(doors))
    contestantBehaviour = random.randint(1,2)

    #Monty door selection
    montySelection = random.randint(1,len(doors))

    while montySelection == contestantSelection or list(doors.values())[montySelection-1] != "Goat":
        montySelection = random.randint(1,len(doors))

    # If contestant select current door, it opens, else, select the one
    #that monty didn't selected
    if contestantBehaviour == 1:

        if list(doors.values())[montySelection-1] == "Goat":
            return "Loss"
        else:
            return "Win"

    else:
        keyMontySelected = list(doors.keys())[montySelection-1]
        keyContestantSelected = list(doors.keys())[contestantSelection-1]

        del doors[keyMontySelected]
        del doors[keyContestantSelected]

        if list(doors.values())[0] == "Goat":
            return "Loss"
        else:
            return "Win"
            
def main():
    print("This program execute Monty Hall game 100,000 times each execution")
    print("The following text shows the percentage of winning and looses of all contestant depending on their choice")
    numLoose= 0
    numWin = 0

    for i in range(0, 100000):
        doors = doorsPosition()
        result = optionSelected(**doors)

        if result == "Loss":
            numLoose = numLoose + 1
        else:
            numWin = numWin + 1 

    print('Winning: '+ str(math.floor((numWin/100000)*100)) + '%')
    print('Loss: '+ str(math.floor((numLoose/100000)*100)) + '%')


if __name__ == "__main__":
    main()
