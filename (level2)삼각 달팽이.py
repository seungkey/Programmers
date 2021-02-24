def solution(n):
    answer = []
    tri=[[]]*n
    for i in range(len(tri)):
        tri[i]=[0]*(i+1)
    a=0
    b=n
    num=1
    tri[0][0]=1
    while(a<=b):
        a+=1
        for i in range(a,b):
            if(tri[i][a-1]==0):
                tri[i][a-1]=tri[i-1][a-1]+1
            if(i==b-1):
                for j in range(a,b-(a-1)):
                    tri[i][j]=tri[i][j-1]+1
        for i in range(b-2,a-1,-1):
            if(tri[i][i-(a-1)]==0):
                tri[i][i-(a-1)]=tri[i+1][i-(a-1)+1]+1
            
        b-=1
    for i in range(len(tri)):
        for j in range(len(tri[i])):
            answer.append(tri[i][j])
    return answer