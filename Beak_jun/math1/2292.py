k=int(input())
if k==1:
  print(1)
else:
  list_ = [7]
  a=7
  b=12
  i=2
  while a<k:
    a=a+b
    list_.append(a)
    b+=6
    i+=1
  print(i)