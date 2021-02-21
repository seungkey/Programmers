def solution(n):
    answer = 0
    li=[0,1]
    for i in range(1,n):
        li.append(li[i-1]+li[i])
    answer=li[n]%1234567   
    return answer