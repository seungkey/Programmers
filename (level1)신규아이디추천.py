import re

def solution(new_id):
    a=new_id.lower()
    d=[]
    b=list(a)
    while len(b)>=1:
        c=b.pop(0)
        if(c=='.' or c=='-' or c=='_' or re.sub('[^a-z0-9]','',c)):
            if(len(b)>=1):
                if(c=='.' and c==b[0]):
                    continue
                else:
                    d.append(c)
            else:        
                d.append(c)
    
    for i in range(len(d)):
        if(d[0]=='.'):
            d.pop(0)
    while(len(d)>=16):
        d.pop(len(d)-1)
    while(len(d)>=1):
        if(d[len(d)-1]=='.'):
            d.pop(len(d)-1)
        elif(d[len(d)-1]!='.'):
            break
    while(len(d)<3):
        if(len(d)==0):
            d.append('a')
        else:
            d.append(d[len(d)-1])
    answer = ''.join(d)
    return answer