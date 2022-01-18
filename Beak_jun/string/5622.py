word = input()
alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
T = 0
for w in word:
  for alp in alphabet:
    for a in alp:
      if w==a:
        T += alphabet.index(alp)+3

print(T)