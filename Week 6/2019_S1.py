#Take the set of flips provided
actions = input()

#Predefine the initial grid
grid = [1, 2, 3, 4]

for action in actions:
	#Horizontal Flip
	if action == "H":
		grid[0], grid[1], grid[2], grid[3] = grid[2], grid[3], grid[0], grid[1]
	else:
		#Vertical Flip
		grid[0], grid[1], grid[2], grid[3] = grid[1], grid[0], grid[3], grid[2]

#Print the resulting grid
print(grid[0], grid[1])
print(grid[2], grid[3])