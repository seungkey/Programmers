def solution(numbers):
    answer = []
    while len(numbers)>=1:
        a=numbers.pop(0)
        for i in range(len(numbers)):
            answer.append(a+numbers[i])
    for k in range(len(answer)):
        b=answer.pop(0)
        for l in range(len(answer)):
            if(b==answer[l]):
                break
        else:
             answer.append(b)
    answer.sort()
    return answer