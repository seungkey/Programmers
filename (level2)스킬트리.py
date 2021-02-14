def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        a=[]
        for j in i:
            for k in skill:
                if(j==k):
                    a.append(j)
        a=''.join(a)
        if(skill[0]==a[0]):
            if(a in skill):
                answer+=1
        
    return answer