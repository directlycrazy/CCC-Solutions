spaces = int(input())

spaceStore = [0] * spaces

for i in range(2):
    #Ask for the each parking space
    space = input()
    for x in range(spaces):
        #If there is a C, note that a car is in the sapce
        spaceStore[x] += 1 if space[x] == "C" else 0

totalOccupied = 0

for x in range(len(spaceStore)):
    #If there are 2 cars in the space for both days, increase #
    if spaceStore[x] == 2: totalOccupied += 1

print(totalOccupied)
