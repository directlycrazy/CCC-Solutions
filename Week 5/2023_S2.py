#number of mountains
N = int(input())

#stores mountain range
mRange = list(map(int, input().split()))
#stores asymmetric values for all crops for all lengths
aValues = [[] for _ in range(N)]

#all crops of length 1 are gonna have asymmetric values of 0
aValues[0] = [0] * N

#iterate through all crop lengths
for i in range(1, N): 

    #crop of length 2
    if i == 1: 
        #iterate through all crops
        for x in range(N-1): 
            #add asymmetric values
            aValues[1].append(abs(mRange[x]-mRange[x+1]))
    
    else: 
        #iterate through all crops
        for x in range(N-i):
            #add asymmetric values using 2 end values and previously calculated asymmetric values
            aValues[i].append(abs(mRange[x]-mRange[x+i]) + aValues[i-2][x+1])

#find and output the lowest asymmetric value for each crop length
for i in range(N): 
    mNum = aValues[i][0]

    for num in aValues[i]:
        mNum = min(num, mNum)
    
    print(mNum, end=" ")
