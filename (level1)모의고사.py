def solution(answers):
    answer = []
    a=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    result=[0]*len(a)
    c=0

    b=len(answers)
    for i in range(len(a)):
        k=0
        while(b>len(a[i])):
            a[i].append(a[i][k])
            k+=1
        for l in range(b):
            if(answers[l]==a[i][l]):
                result[i]+=1
    for j in range(len(result)):
        if(result[j]==max(result)):
            answer.append(j+1)
        
                
    return answer