#Collect the number of peppers
numPeppers = int(input())

#Create lists for the peppers and their respective scoville heat levels
peppers = ["Poblano", "Mirasol", "Serrano", "Cayenne", "Thai", "Habanero"]
scovilleHeat = [1500, 6000, 15500, 40000, 75000, 125000]

#Declare the total heat of all combined peppers
totalHeat = 0

for x in range(numPeppers):
	#Ask for the name of the pepper
	pepperName = input()
	
	#Add the heat of the pepper to the total heat (index of the pepper name in the first array is the same as its heat in the second array)
	totalHeat += scovilleHeat[peppers.index(pepperName)]

#Output the total heat
print(totalHeat)