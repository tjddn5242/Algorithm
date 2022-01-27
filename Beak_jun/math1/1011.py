T = int(input())
LL = [1,2]
for _ in range(T):
  x,y = map(int, input().split())
  k=y-x
  if k==1 or k==2:
    print(LL[k-1])
  else:
    j=2
    for i in range(3,k+1,2):
      LL.extend([i for _ in range(j)])
      LL.extend([i+1 for _ in range(j)])
      j += 1
    print(LL[k-1])
