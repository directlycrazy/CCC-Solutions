numFriends = int(input())

friends = [[0, 0, 0]] * numFriends

#Called a "number line," use binary search since sorted
left = 1000000000
right = 0

for x in range(numFriends):
	values = input().split(" ")
	#Initial Pos, Walking Rate m/s, Hearing Distance 
	friends[x] = [int(values[0]), int(values[1]), int(values[2])]
	right = max(right, friends[x][0])
	left = min(left, friends[x][0])

mid = (left + right) / 2

def calculateTime(pos):
	totalTime = 0

	for x in range(numFriends):
		#Absolute of their desired pos - current pos, - hearing distance, and multiply by rate in m/s to find time taken per metre traveled
		totalTime += (max(abs(pos - friends[x][0]) - friends[x][2], 0) * friends[x][1])

	return totalTime

while True:
	leftTime = calculateTime(mid - 1)
	rightTime = calculateTime(mid + 1)
	currentTime = calculateTime(mid)

	#Compare times and directions to move along the number line
	if leftTime < currentTime:
		right = mid
		mid = (left + mid) / 2
	elif rightTime < currentTime:
		left = mid
		mid = (right + mid) / 2
	else:
		print(int(currentTime))
		break