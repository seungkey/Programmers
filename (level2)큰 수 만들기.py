def solution(number, k):
    a=list(number)
    while(len(a)>len(number)-k):
        for i in range(len(number)-1):
            if(a[i]<a[i+1]):
                del a[i]
                break
    answer=''.join(a)
    return answer