M = int(input())
N = M
cycle=0

while True:
  if N<10:
    N=10*N+N
  else:
    first=N%10
    second=N%10+N//10
    if second>9:
      second = second-10
    else:
      second = second
    N=10*first+second
  if N==M:
    break
  else:
    cycle+=1

print(cycle+1)