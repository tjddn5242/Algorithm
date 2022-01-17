word = input().upper()
cnt = []
for w in list(set(word)):
  cnt.append(word.count(w))

if cnt.count(max(cnt))>1:
  print('?')
else:
  print(list(set(word))[cnt.index(max(cnt))])