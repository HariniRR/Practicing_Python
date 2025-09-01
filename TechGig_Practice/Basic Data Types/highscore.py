#The score of N players is given and you have to find the highest score of an individual.
N = int(input())
scores = []
for i in range(N):
    score = int(input())
    scores.append(score)
print(max(scores))