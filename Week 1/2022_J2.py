#Number of players input from grader
numPlayers = int(input())

#Track number of gold players
goldPlayers = 0

#Ask for scores for each player
for i in range(numPlayers):
	#Number of points the player scored and fouls

	#For each scored point, they will have a weight of 5 pts adding to their score
	scoredPoints = int(input()) * 5
	
	#For each foul, they will have a weight of 3 pts decreasing their score
	fouls = int(input()) * 3

	if scoredPoints - fouls > 40: goldPlayers += 1

# Display number of players that are gold
# Also an additional plus if the team is gold (all players are gold: goldPlayers = numPlayers)
print(str(goldPlayers) + "+" if goldPlayers == numPlayers else str(goldPlayers))