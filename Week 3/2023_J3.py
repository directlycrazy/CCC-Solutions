#Get the total number of attendees
totalAttendees = int(input())

#Create a blank list to store the number of guests for each day
numGuests = [0] * 5

#Create a variable to store the highest number of attendees a day has
mostAttendees = 0

for x in range(totalAttendees):
	#Get the schedule of the guests
	schedule = input()

	#Increment the number of guests a day has based on their schedule
	for i in range(len(schedule)):
		#"Add 1 if the guest has marked 'Y' and 0 if otherwise"
		numGuests[i] += 1 if schedule[i] == "Y" else 0

#Create a list to store the days with the most attendees
largestDays = []

for i in range(len(numGuests)):
	day = numGuests[i]

	#Check if the # of attendees on the current day is larger than the previous largest day
	if day > mostAttendees:
		#Set the current day as the largest day
		mostAttendees = day
		#Overwrite the array with the new largest day
		largestDays = [str(i + 1)]
	elif day == mostAttendees:
		#If the current day is the most number of attendees, add it to the array
		#Since the array is overwritten if the day is larger than the largest number of attendees, we can assume that the additional days we are adding now always have the most people
		largestDays.append((str(i + 1)))

#Join the array of days in the specific requested format from the CCC
print(",".join(largestDays))