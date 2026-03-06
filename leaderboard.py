scores = []
alice = []

n = int(input("Enter number of leaderboard scores: "))

print("Enter leaderboard scores:")
for i in range(n):
    scores.append(int(input()))

m = int(input("Enter number of Alice scores: "))

print("Enter Alice scores:")
for i in range(m):
    alice.append(int(input()))

unique_scores = []

for s in scores:
    if s not in unique_scores:
        unique_scores.append(s)

for a in alice:
    rank = 1
    for s in unique_scores:
        if a < s:
            rank += 1
    print(rank)