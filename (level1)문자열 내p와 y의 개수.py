def solution(s):
    answer = True
    p_num=0
    y_num=0
    s=s.lower()
    for i in range(len(s)):
        if(s[i]=='p'):
            p_num+=1
        elif(s[i]=='y'):
            y_num+=1
        else:
            continue
    if(p_num==y_num):
        answer=True
    elif(p_num!=y_num):
        answer=False
    return answer