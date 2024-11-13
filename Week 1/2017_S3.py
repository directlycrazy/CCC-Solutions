
#get input
pieces = int(input())    
lengths = map(int, input().split())

#initialize array to store inventory of boards
inventory = [0] * 2001

#populate inventory
for length in lengths:
    inventory[length] += 1

#variables to store output variables
max_length = 0
length_count = 0

#iterate through all possible fence heights
for i in range(2, 4001):

    #create a temporary array to use for each fence height
    invetory_copy = inventory.copy()

    #set starting points for where boards added equal the fence height (i)
    left = max(1, i - 2000)
    right = i - left

    #initialize variable that stores the length of fence height (i)
    length = 0

    #iterate through all possible board combinations that result in the fence height (i)
    while left <= (i // 2):

        #if pointing to the same board length, just divide by 2 and add it to fence length
        if left == right:
            num_boards = invetory_copy[left] // 2
            invetory_copy[left] -= num_boards * 2
            length += num_boards

        #take the lowest number of boards between the two board lengths and add that number to length
        else:
            num_boards = min(invetory_copy[left], invetory_copy[right])
            invetory_copy[left] -= num_boards
            invetory_copy[right] -= num_boards
            length += num_boards

        #move to the next combination of board lengths
        left += 1
        right -= 1

    #update max length
    if length > max_length:
        max_length = length
        length_count = 0

    #update length
    if length == max_length:
        length_count += 1

#output variables
print(max_length, length_count)