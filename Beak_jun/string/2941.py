change=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = 'ljes=njak'
num=0
for i in range(len(word)):
  if word[i]+word[i+1] in change:
    word[i+1]='0'
    num += 1
  
