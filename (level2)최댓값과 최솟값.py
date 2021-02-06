def solution(s):
    answer = ''
    a=s.split()
    b=[]
    for i in range(len(a)):
        b.append(int(a[i]))
    answer=str(min(b))+' '+str(max(b))
    return answer