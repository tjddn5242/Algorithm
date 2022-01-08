N = 1
for _ in range(3):
  m = int(input())
  N=N*m

N = list(str(N))

for i in range(0,10):
  print(N.count(str(i)))