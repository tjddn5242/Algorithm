S = list(input())
S = [ord(i)-96 for i in S]
# print(S)
answer = [-1 for _ in range(26)]

for idx, i in enumerate(S):
  if answer[i-1]==-1:
    answer[i-1]=idx

for i in answer:
  print(i, end=' ')