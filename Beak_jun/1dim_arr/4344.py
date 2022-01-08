C = int(input())
for _ in range(C):
  score = list(map(int,input().split()))
  N = score.pop(0)
  mean_score = sum(score,0.0)/N
  count = 0
  for i in score:
    if i>mean_score:
      count+=1
  ratio=(count/N)*100
  print(f'{ratio:.3f}%')