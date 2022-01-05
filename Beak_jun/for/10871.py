import sys
N,X = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))

for a in A:
  if a < X:
    print(a, end=' ')