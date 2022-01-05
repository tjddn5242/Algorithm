import sys
T = int(sys.stdin.readline().rstrip())
for t in range(T):
  a,b = map(int, sys.stdin.readline().rstrip().split())
  print(f"Case #{t+1}: {a} + {b} = {a+b}")