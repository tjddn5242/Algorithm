T = int(input())
for _ in range(T):
  H, W, N = map(int, input().split())
  num = []
  for w in range(1,W+1):
    for h in range(1,H+1):
      num.append(h*100+w)
      if len(num)==N:
        print(num[-1])
        break