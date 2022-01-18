a, b = input().split()
a_num=0; b_num=0

for i,j in enumerate(a):
  j=int(j)
  a_num += j*(10**(i))
for i,j in enumerate(b):
  j=int(j)
  b_num += j*(10**(i))

if a_num>b_num:
  print(a_num)
elif a_num<b_num:
  print(b_num)