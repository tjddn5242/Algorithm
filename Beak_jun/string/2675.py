T = int(input())
for l in range(T):
  answer = []
  RS = input().split()
  R = int(RS[0])
  S = list(RS[1])
  for i in S:
    for _ in range(R):
      answer.append(i)
  print(''.join(answer))
