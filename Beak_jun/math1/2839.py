N = int(input())
unav = [1,2,4,7]
if N in unav:
  print(-1)
elif (N%5)==0:
  print(N//5)
elif (N%5)==1:
  print((N//5-1)+2)
elif (N%5)==2:
  print((N//5-2)+4)
elif (N%5)==3:
  print((N//5)+1)
elif (N%5)==4:
  print((N//5-1)+3)
