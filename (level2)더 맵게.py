import heapq
def solution(scoville, K):
    answer = -1
    count = 0
    flag = False;
    a=[]
    for i in scoville:
        heapq.heappush(a,i)
    while(a[0]<K):
        heapq.heappush(a,(heapq.heappop(a)+(heapq.heappop(a)*2)))
        if(len(a)==1 and a[0]<K):
            flag = True
            break
        count+=1
    if(flag==False):
        answer=count
    return answer