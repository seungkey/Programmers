def solution(n):
    answer = []
    tri=[[]]*n
    for i in range(len(tri)):
        tri[i]=[0]*(i+1)
    a=0
    b=n
    tri[0][0]=1
    while(a<b):
        a+=1
        for i in range(a,b):
            if(tri[i][a]!=0):
                pass
            else:
                tri[i][a-1]=tri[i-1][a-1]+1
                #if(i==b-1):
                 #   for j in range(a,b):
                  #      tri[i][j]=tri[i][j-1]+1    
                
        b-=1
        for i in range(b-1,a-1,-1):
            tri[i][i]=tri[i+1][i+1]+1
        
        
    print(tri)
    return answer