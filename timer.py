import time
import random

chosenTime = 5

def timer():
    guessMade = False
    startTime = time.time()  # starts timer
    finishTime = time.time()
    maxTime = startTime + chosenTime
    while finishTime <= maxTime and guessMade == False:
        finishTime = time.time()
        print(finishTime - startTime)
        if round(finishTime - startTime) == 3:
            guessMade = False
        print("Answered with", int(chosenTime - finishTime), "seconds left")
    else:
        print("Answered with", int(maxTime - finishTime), "seconds left")

timer()