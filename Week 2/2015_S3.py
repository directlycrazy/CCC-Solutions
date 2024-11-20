#Take the number of gates at the airport, and planes which will land 
gates = int(input())
planes = int(input())

#Create a list of gates with all gates open
gatesList = [0]*gates
result = 0

#Ask which gate each plane should dock at
for i in range(planes):
	plane = int(input()) - 1

	while plane >= 0 and gatesList[plane] > 0:
		temp = gatesList[plane]
		gatesList[plane] += 1
		plane = plane - temp

	if plane < 0:
		break
	else:
		gatesList[plane] += 1
		result += 1

print(result)