def solution(nums):
    answer = 0
    choice=[]
    nums.sort()
    choice.append(nums[0])
    for i in range(1,len(nums)):
        if(nums[i-1]!=nums[i]):
            choice.append(nums[i])
    if(len(choice)<=int(len(nums)/2)):
        answer=len(choice)
    else:
        answer=int(len(nums)/2)
    return answer