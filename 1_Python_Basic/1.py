# Python 자료형

# 정수형
a = 100;
print(a)

# 실수형
b = 1e9
print(b)
print(0.3+0.6)
print(round(123.456,1))
print(round(0.3+0.6,4))

# 연산자
print("=====연산자=====")
print(5+3)
print(5**3) # 거듭제곱
print(5/3) # 나누어서 실수 형으로
print(5//3) # 몫
print(5%3) # 나머지

# 리스트
print("=====리스트=====")
a = [] # 빈 리스트 선언
print(a)

n = 10
a = [0] * n
print(a) # 크기가 n인 1차원 리스트 생성

a = [i+1 for i in range(10)] # 리스트 컴프리핸션
print(a)
a = [i for i in range(10) if i%2==0]
print(a)

print(a[1:3]) # 리스트 인덱싱

n=3
m=4
a = [[0] * m for _ in range(n)] # nxm인 리스트 생성
print(a)

l = [1,4,3]
print(l)
l.append(2) # 값 추가
print(l) 
l.sort() # 정렬
print(l) 
l.sort(reverse=True) # 역정렬
print(l)
l.reverse() # 순서 뒤집기
print(l) 
l.insert(2,3) # 해당 인덱스(2)에 값(3) 추가
print(l) 
print(l.count(3)) # 원소가 3인 것의 개수
l.remove(3) # 특정 원소 제거
print(l)


# 특정 원소 지울 때
a = [1,2,3,4,5,5,5]
remove_set = [3,5]

result = [i for i in a if i not in remove_set]
print(result)

# 문자열
print("=====문자열=====")
data = 'Hello World!'
print(data)
data = "Hello \"world!\""
print(data)

a = 'Hello'; b = 'World!'
print(a+' '+b)

c = 'String'
print(c*3)

a = "ABCDE"
print(a[2:4])

# 사전형
print("=====사전형=====")
a = dict() # 빈 사전형 선언
a['사과'] = 'Apple'
a['바나나'] = 'Banana'
a['코코넛'] = 'Coconut'
print(a)

if '사과' in a:
  print('사과 존재')

print(a.keys())
print(a.values())


# 집합형
data = set([1,2,2,3,4,5,5,5]) # 집합 선언1
print(data)

data = {1,2,2,3,4,5,5,5} # 집합 선언2
print(data)

a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(a|b) # 합집합
print(a&b) # 교집합
print(a-b) # 차집합

data = {1,2,3}
data.add(4) # 원소 추가
print(data)
data.update([5,6]) # 두개 이상의 원소 추가
print(data)
data.remove(3) # 원소 삭제
print(data)

# 조건문
print("=====조건문=====")
score = 85
if score >= 80:
  pass
else:
  print('85 미만')

print('프로그램 종료')

if score >= 80: print('Success')
else: ('Fail')

result = "Success" if score >= 80 else "Fail"
print(result)

