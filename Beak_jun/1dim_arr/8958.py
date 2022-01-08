def answer(L):
  rep=[]
  count=0
  for l in L:
    if l=='X':
      count=0
      rep.append(count)
    else:
      count+=1
      rep.append(count)
  return (sum(rep))
T = int(input())
for i in range(T):
  L=list(input())
  print(answer(L))