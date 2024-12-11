#length of pathway
l = int(input())

#lists to store tiles
t = list(map(int, input().split()))
b = list(map(int, input().split()))

#count for meters of tape
count = 0 

#iterate through tiles on top
for i in range(l): 
    #if current tile is painted
    if t[i] == 1: 
        #add three sides
        count += 3

        #if there is a tile on the left remove a side
        if i < l-1:
            if t[i+1] == 1: 
                count -= 1
        
        #if there is a tile on the right remove a side
        if i > 0: 
            if t[i-1] == 1:
                count -= 1
        
        #if there is a tile on the bottom remove a side (only every second tile)
        if i % 2 == 0: 
            if b[i] == 1:
                count -= 1

#iterate through tiles on bottom
for i in range(l): 
    #if current tile is painted
    if b[i] == 1: 
        #add three sides
        count += 3

        #if there is a tile on the left remove a side
        if i < l-1:
            if b[i+1] == 1: 
                count -= 1
        
        #if there is a tile on the right remove a side
        if i > 0: 
            if b[i-1] == 1:
                count -= 1
        
        #if there is a tile on the bottom remove a side (only every second tile)
        if i % 2 == 0: 
            if t[i] == 1:
                count -= 1

#output meters of tape
print(count)
