def solution(people, limit):
    answer = 0
    save=[]
    a=0
    boat=[]
    people.sort()
    while(len(people)>0):
        a=0
        a=sum(boat)
        a+=people[0]
        if(a<=limit and len(boat)<2):
            boat.append(people.pop(0))
        elif(a>limit or len(boat)>=2):
            save.append(boat)
            boat=[]
        print(a,boat,save)
    answer=len(save)+1
    return answer