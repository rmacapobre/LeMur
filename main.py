import random
import subprocess

def HowManySoldiers():
    ok = False
    while not ok:
        try:
            # How many soldiers?
            answer = input("How many soldiers? ")
            count = int(answer)
            ok = True
            return count
        except ValueError:
            print("Please enter a number.")

def GetSoldierNames(count):
    names = []
    for x in range(count):
        name = input("What is your name soldier? ")
        names.append(name)
    return names

def DisplayRound(round):
    print("=============================================")
    print("ROUND ", round+1)
    print("=============================================")


def DisplayRemainingMembers(names):
    print("Remaining Members:")
    print("\t", names)

def DisplayFinalResult(names):
    print("=============================================")
    print("FINAL RESULT")
    print("=============================================")
    print("\t", names[0], " will go seek for reinforcements ")


subprocess.call(["ls", "-l"])

# How many soldiers?
soldierCount = HowManySoldiers()

# Get the soldier names
names = GetSoldierNames(soldierCount)

# Determine who will go seek for reinforcements
round = 0
while soldierCount > 1:
    DisplayRound(round)
    DisplayRemainingMembers(names)

    # Remove the soldier from the list
    draw = random.randint(0, soldierCount-1)
    print(names[0], " has eliminated ", names[draw])
    del names[draw]

    round += 1
    soldierCount -= 1

# Final Result
DisplayFinalResult(names)