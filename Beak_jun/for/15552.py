import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
  b,c = map(int, sys.stdin.readline().rstrip().split())
  print(b+c)
