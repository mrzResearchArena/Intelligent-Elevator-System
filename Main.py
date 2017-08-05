from random import uniform  # uniform distribution
import itertools  # Combination
import math  # floor 0r celling
import time  # time counter

global totalServed
totalServed = 0

global up
up = []
global down
down = []

global upStop
upStop = []
global downStop
downStop = []

global currentLocation
currentLocation = 1

global currentWeight
currentWeight = 0.0

global elevatorDirection
elevatorDirection = "up"

global serverStatus
serverStatus = "idle"  # "busy"

global N
N = 6


def generateWeight():
    p = uniform(0.0, 1.0)

    if 0.0 <= p < 0.10:
        instanceWeight = uniform(25, 30)
    elif 0.10 <= p < 0.20:
        instanceWeight = uniform(30, 50)
    elif 0.20 <= p < 0.60:
        instanceWeight = uniform(50, 70)
    elif 0.60 <= p < 0.85:
        instanceWeight = uniform(70, 90)
    elif 0.90 <= p < 0.95:
        instanceWeight = uniform(90, 100)
    else:
        instanceWeight = uniform(100, 120)

    return math.ceil(instanceWeight)


def personCount(i, direction):
    value = uniform(0.0, 1.0)

    if direction == "up":
        if i == 1:

            if 0.00<= value < 0.20:
                return 0
            elif 0.20 <= value < 0.40:
                return 1
            elif 0.40 <= value < 0.60:
                return 2
            elif 0.60 <= value < 0.80:
                return 3
            elif 0.80 <= value < 0.90:
                return 4
            elif 0.90 <= value < 0.95:
                return 5
            else:
                return 6


        elif i == 2:

            if 0.00 <= value < 0.30:
                return 1
            elif 0.30 <= value < 0.40:
                return 2
            elif 0.40 <= value < 0.60:
                return 3
            elif 0.60 <= value < 0.80:
                return 4
            elif 0.80 <= value < 0.90:
                return 5
            elif 0.90 <= value < 0.95:
                return 6
            else:
                return 0



        elif i == 3:

            if 0.00 <= value < 0.40:
                return 1
            elif 0.40 <= value < 0.60:
                return 2
            elif 0.60 <= value < 0.80:
                return 3
            elif 0.80 <= value < 0.85:
                return 4
            elif 0.85 <= value < 0.90:
                return 5
            elif 0.90 <= value < 0.95:
                return 6
            else:
                return 0


        elif i == 4:

            if 0.00 <= value < 0.60:
                return 1
            elif 0.60 <= value < 0.75:
                return 2
            elif 0.75 <= value < 0.80:
                return 3
            elif 0.80 <= value < 0.85:
                return 4
            elif 0.85 <= value < 0.90:
                return 5
            elif 0.90 <= value < 0.95:
                return 6
            else:
                return 0


        elif i == 5:
            if 0.00 <= value < 0.60:
                return 0
            elif 0.60 <= value < 0.75:
                return 1
            elif 0.75 <= value < 0.80:
                return 2
            elif 0.80 <= value < 0.85:
                return 3
            elif 0.85 <= value < 0.90:
                return 4
            elif 0.90 <= value < 0.95:
                return 5
            else:
                return 6

    else:
        if i == 6:
            if 0.0 <= value < 0.30:
                return 6
            elif 0.30 <= value < .50:
                return 5
            elif 0.50 <= value < .70:
                return 4
            elif 0.70 <= value < .80:
                return 3
            elif 0.80 <= value < .90:
                return 2
            elif 0.90 <= value < 0.95:
                return 1
            else:
                return 0

        if i == 5:

            if 0.0 <= value < 0.30:
                return 6
            elif 0.30 <= value < .50:
                return 5
            elif 0.50 <= value < .70:
                return 4
            elif 0.70 <= value < .80:
                return 3
            elif 0.80 <= value < .90:
                return 2
            elif 0.90 <= value < 0.95:
                return 1
            else:
                return 0


        if i == 4:

            if 0.0 <= value < 0.30:
                return 6
            elif 0.30 <= value < .50:
                return 5
            elif 0.50 <= value < .70:
                return 4
            elif 0.70 <= value < .80:
                return 3
            elif 0.80 <= value < .90:
                return 2
            elif 0.90 <= value < 0.95:
                return 1
            else:
                return 0

        if i == 3:

            if 0.0 <= value < 0.10:
                return 6
            elif 0.10 <= value < 0.20:
                return 5
            elif 0.30 <= value < 0.40:
                return 4
            elif 0.40 <= value < 0.75:
                return 3
            elif 0.75 <= value < 0.85:
                return 2
            elif 0.85 <= value < 0.90:
                return 1
            else:
                return 0


        if i == 2:
            if 0.0 <= value < 0.03:
                return 6
            elif 0.03 <= value < 0.06:
                return 5
            elif 0.06 <= value < 0.09:
                return 4
            elif 0.09 <= value < 0.12:
                return 3
            elif 0.12 <= value < 0.15:
                return 2
            elif 0.15 <= value < 0.30:
                return 1
            else:
                return 0


def settingUp(i):
    value = []
    while i < 7:
        value.append(i)
        i = i + 1

    return value


def settingDown(i):
    value = []
    while i > 0:
        value.append(i)
        i = i - 1

    return value


def process():
    global up
    global down

    up.append([])
    down.append([])

    i = 1
    while i < 6:
        value = settingUp(i + 1)
        up.append(value)
        i = i + 1

    i = 6
    while i > 0:
        value = settingDown(i - 1)
        down.append(value)
        i = i - 1


def ensureStop():
    upStop.append(0)
    downStop.append(0)

    i = 1
    while i < 7:
        upStop.append(0)
        downStop.append(0)
        i = i + 1


def intelligenceDistribution(currentLocation, elevatorDirection):

    p = uniform(0.0, 1.0)

    if elevatorDirection == "up":

        if currentLocation == 1:
            if 0.0 <= p <= 0.03:
                return 2
            elif 0.04 <= p <= 0.34:
                return 3
            elif 0.35 <= p <= 0.75:
                return 4
            elif  0.76 <= p <= 0.95:
                return 5
            else:
                return 6

        elif currentLocation == 2:
            if 0.0 <= p <= 0.03:
                return 3
            elif 0.04 <= p <= 0.54:
                return 4
            elif  0.55 <= p <= 0.95:
                return 5
            else:
                return 6

        elif currentLocation == 3:
            if 0.0 <= p <= 0.05:
                return 4
            elif 0.05 <= p <= 0.90:
                return 5
            else:
                return 6

        elif currentLocation == 4:
            if 0.0 <= p <= 0.05:
                return 5
            else:
                return 6

        else:
            return 6

    # When elevatorDirection is down.

    else:
        if currentLocation == 6:
            if 0.0 <= p <= .67:
                return 1
            elif 0.68 <= p <= 0.78:
                return 2
            elif 0.79 <= p <= .88:
                return 3
            elif 0.89 <= p <= .97:
                return 4
            else:
                return 5

        elif currentLocation == 5:
            if 0.0 <= p <= .67:
                return 1
            elif 0.68 <= p <= 0.78:
                return 2
            elif 0.79 <= p <= .95:
                return 3
            else:
                return 4

        elif currentLocation == 4:
            if 0.0 <= p <= .75:
                return 1
            elif 0.76 <= p <= 0.95:
                return 2
            else:
                return 3


        elif currentLocation == 3:
            if 0.0 <= p <= .95:
                return 1
            else:
                return 2

        elif currentLocation == 2:
            return 1


def main():
    process()
    ensureStop()

    min = int(input())
    end = time.time() + 60.0 * min


    global N
    global currentLocation
    global elevatorDirection
    global currentWeight
    global serverStatus
    global totalServed

    serverStatus = "busy"

    while time.time() < end:

        runningCar = []  # This a carrying car.

        if elevatorDirection == "up":

            # person need to modify
            person = personCount(currentLocation, elevatorDirection)  # Total person takes

            if person > 0:
                time.sleep(5.0)

            i = 0

            while i < person:

                if currentWeight <= 550.0:  # Maximum can carry upto 750.0, when up.

                    liftPosition = intelligenceDistribution(currentLocation, elevatorDirection)

                    upStop[liftPosition] = 1

                    weight = generateWeight()

                    currentWeight = currentWeight + weight  # Weight in increasing

                    runningCar.append((weight, liftPosition))  # This is a tupple [ like class ]

                # Need to edit
                else:
                    if currentWeight == 0:
                        serverStatus = "idle"
                    else:
                        break

                i = i + 1

            currentLocation += 1
            time.sleep(1.5) # Takes 1.5 seconds for going next steps

            if upStop[currentLocation] == 1:

                time.sleep(5.0)

                for I in runningCar:

                    if I[1] == currentLocation:
                        weight -= I[0]

                        runningCar.remove(I)

                        totalServed += 1


            # Special Checking ... elevatorDirection will change up to down.
            # N = 6
            if currentLocation == N:
                elevatorDirection = "down"
                i=1
                while i<=N:
                    upStop[i] = 0
                    i += 1

                # weight will be -> 0.0

                # People can change decetion


        else:

            # person need to modify
            person = personCount(currentLocation, elevatorDirection)  # Total person takes

            if person > 0:
                time.sleep(5.0)

            i = 0

            while i < person:

                if currentWeight <= 550.0:  # Maximum can carry upto 850.0, when down.

                    liftPosition = intelligenceDistribution(currentLocation, elevatorDirection)


                    downStop[liftPosition] = 1

                    weight = generateWeight()


                    currentWeight = currentWeight + weight  # Weight in increasing


                    runningCar.append((weight, liftPosition))  # This is a tupple [ like class ]

                # Need to edit
                else:

                    if currentWeight == 0:
                        serverStatus = "idle"
                    else:
                        break

                i = i + 1

            currentLocation -= 1
            time.sleep(1.5)  # Takes 1.5 seconds for going next steps



            if downStop[currentLocation] == 1:

                time.sleep(5.0)

                for I in runningCar:

                    if I[1] == currentLocation:
                        weight -= I[0]

                        runningCar.remove(I)

                        totalServed += 1

            # Special Checking ... elevatorDirection will change up to down.
            # N = 6
            if currentLocation == 1:
                elevatorDirection = "up"
                i = 1
                while i <= N:
                    downStop[i] = 0
                    i += 1

                    # weight will be -> 0.0

                    # People can change decetion

    print("Total people served {} within {} minute.".format(totalServed, min))


if __name__ == "__main__":
    main()
