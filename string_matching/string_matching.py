def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0]*M

    computeLPS(pat, lps)

    i = 0  
    j = 0  
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == M:
            list_.append(pat)
            list_.append(i-j)
            j = lps[j-1]

def computeLPS(pat, lps):
    leng = 0

    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else: 
                lps[i] = 0
                i += 1

def question1(S, list_):
    Q1=set()
    for i in range(0,len(list_),2):
        Q1.add(list_[i])
    answer1=[]
    for s in S:
        if s in Q1:
            answer1.append('YES')
        else:
            answer1.append('NO')
    return answer1


def question2(S, list_):
    answer2=dict()
    rev_list_ = list(reversed(list_))
    for i in range(1,len(list_),2):
        answer2[rev_list_[i]]=rev_list_[i-1]

    for j in list(reversed(list(answer2.keys()))):
        print(f'#pos={answer2[j]},pattern={j}')

def question3(S, list_):
    for i in range(1,len(list_),2):
        print(f'#pos={list_[i]},pattern={list_[i-1]}')


N = int(input('문자열 집합 S의 원소 개수: '))
S = []
for _ in range(N):
    s = input()
    S.append(s)

print('\n')

Q = int(input('매칭 대상 문자열 수: '))

for _ in range(Q):
    q = input()
    list_=[]
    for s in S:
        KMPSearch(s, q)

    print('\n[Question1]')
    print(question1(S, list_))

    print('\n[Question2]')
    question2(S, list_)

    print('\n[Question3]')
    question3(S, list_)
    # print(f'\n[Question3]\n{question3(S, list_)}')
    # for i in question2(S, q).keys():
    #     print(f'#pos = {question2(S, q)[i]}, pattern = {i}')