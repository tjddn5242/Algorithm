N = []
for i in range(9):
  a = int(input())
  N.append(a)
print(max(N))
print(N.index(max(N))+1)