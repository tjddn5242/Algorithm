T = int(input())
for _ in range(T):
  x,y = map(int, input().split())
  k=y-x
  i=0
  while True:
    if i**2>k:
      break
    else:
      i+=1
  if i**2-i>k:
    print(i-1)
  else:
    print(i)