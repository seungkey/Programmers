def solution(s):
    answer = 0
    a_len=[]
    c=1
    length=len(s)
    for i in range(length):
        a=[]
        b=[]
        j=i+1
        k=0
        while j<=length:
            a.append(s[k:j])
            k+=(i+1)
            j+=(i+1)
        a.append(s[k:])
        while len(a)>1:
            if(a[0]==a[1]):
                c+=1
                a.pop(0)
            else:
                if(c>1):
                    b.append(str(c))
                    b.append(a.pop(0))
                else:
                    b.append(a.pop(0))
                c=1
        b.append(a.pop(0))    
        a_len.append(len(''.join(b)))
    answer=min(a_len)
    return answer