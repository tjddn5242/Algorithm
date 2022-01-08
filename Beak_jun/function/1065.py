N = int(input())
HS = [i for i in range(1,100)]
for l in range(1,10): # 100의 자리
  for m in range(-9,10): # 공차
    if (l+m<=9) and (l+m>=0) and (l+2*m<=9) and (l+2*m>=0):
      HS.append(100*l+10*(l+m)+(l+2*m))


# print(HS)
for idx,k in enumerate(HS):
  if k<=N:
    answer = idx + 1
    

print(answer)