#Take input for number of bids
numBids = int(input())

#Define a set of people 
people = []

#Highest bid amount, and index of the person who provided it
highestBid = 0
highestBidI = 0

#Iterate number of bids
for i in range(numBids):
	#Take the bidder's name and bid amount
	name = input()
	bid = int(input())

	#Add the person to the list of people
	people.append(name)

	#If the bid is higher than the highest bid, update the highest bid and the index of the person
	#This also ensures that if two bids are the same, the first highest bidder will win
	if bid > highestBid:
		highestBid = bid
		highestBidI = i

#Print the name of the person who had the highest bid, using the index of the highest bid
print(people[highestBidI])
