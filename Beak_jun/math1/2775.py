T = int(input())
for _ in range(T):
  K = int(input())
  N = int(input())
  for k in range(K+1):
    if k!=0:
      prev = now
      now = []
    else:
      prev = []
      now = [i for i in range(1,N+1)]
      continue
    for n in range(1,N+1):
      if n!=1:
        now.append(now[-1]+prev[n-1])
      else:
        now.append(1)
  print(now[-1])