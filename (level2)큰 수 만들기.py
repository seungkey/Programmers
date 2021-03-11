def solution(number, k):
    a=[number[0]]
    for i in number[1:]:
        while len(a)>0 and a[-1]<i and k>0:
            k-=1
            a.pop()
        a.append(i)
    a=a[:-k] if k>0 else a
    answer=''.join(a)
    return answer