from itertools import permutations
def solution(numbers):
    answer = 0
    a=[]
    b=[]
    for j in range(len(numbers)):
        for i in permutations(numbers,j+1):
            if(int(''.join(i)) not in a):
                a.append(int(''.join(i)))
    for k in range(len(a)):
        for i in range(2,a[k]):
            if(a[k]%i==0):
                break
        else:
            b.append(a[k])
    b.sort()
    while(0 in b or 1 in b):
        del b[0]
    answer=len(b)
    return answer