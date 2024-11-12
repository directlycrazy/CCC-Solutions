#Gather inputs for m, n, and k values
m = int(input())
n = int(input())
k = int(input())

#Generate the grid of rows and cols
rows = [0]*m
cols = [0]*n

#Get each choice from the artist
for i in range(k):
	action = input().split()
	direction = action[0]
	#Numbers can be given such as "1" indicating row 0
	index = int(action[1]) - 1

	if direction == 'R':
		rows[index] += 1
	else: 
		cols[index] += 1

#Count of gold cells on the canvas
count = 0

for i in range(m):
	for v in range(n):
		#Add the number of times the value has been overwritten and check if is even
		#Ex. row = 1, col = 2 would be gold, since it has been painted 3 times (gold, not gold, gold)
		#row = 1, col = 1 would not be gold, since it has been painted once, and reverted back (gold, not gold)
		if (rows[i] + cols[v]) % 2 == 1:
			count += 1

print(count)