X = int(input())
# 몇 번째 대각선에 있는지?
line = 1
while X>line:
  X-=line
  line+=1
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')