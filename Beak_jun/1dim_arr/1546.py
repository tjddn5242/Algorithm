N = int(input())
score = list(map(int, input().split()))
fake_score = []
for i in score:
  fake_score.append((i/max(score))*100)

print(sum(fake_score)/N)