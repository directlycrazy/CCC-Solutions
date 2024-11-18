#number of lines
N = int(input())

#variables to store number of each character
t = 0
s = 0

#process each line
for i in range(N): 
    line = input()
    
    #process each character and increase number of "s" and "t"
    for char in line: 
        if char.lower() == "s": 
            s += 1
        elif char.lower() == "t": 
            t += 1

#determine if it is french or english by comparison
if s >= t: 
    print("French")
else: 
    print("English")