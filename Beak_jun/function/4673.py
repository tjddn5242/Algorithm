n=10000
def generate(k):
  L = map(int, list(str(k)))
  return sum(L)+k

generated=set()
all_num = set([i for i in range(1,n+1)])

for i in range(1,n-10):
  generated.add(generate(i))

result=all_num-generated
result = list(result)
result.sort()

for i in result:
  print(i)