participants = int(input())

scores = [0] * participants
rawScores = [0] * participants

for x in range(participants):
	score = int(input())
	rawScores[x] = score
	if score not in scores:
		scores[x] = score

scores.sort()

bronzeScore = scores[-3]
numDuplicates = rawScores.count(bronzeScore)

print(bronzeScore, numDuplicates)