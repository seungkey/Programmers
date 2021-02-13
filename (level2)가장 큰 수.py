def solution(numbers):
    answer = ''
    a=[]
    for i in numbers:
        i=str(i)
        a.append(i*3)
    a.sort(reverse=True)
    for j in range(len(a)):
        b=int(len(a[j])/3)
        a[j]=a[j][:b]
    answer=str(int(''.join(a)))
    return answer