#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(board, moves):
    answer = 0
    a=0
    result=[]
    loop=len(moves)
    while len(moves)>=1:
        i=moves.pop(0)
        for j in range(len(board)):
            if(board[j][i-1]!=0):
                if(a==board[j][i-1]):
                    answer+=2
                    result.pop()
                else:
                    result.append(board[j][i-1])
                a=board[j][i-1]
                board[j][i-1]=0
                break
            else:
                continue
    for l in range(loop):
        for m in range(len(result)):
            if(m+1<len(result)):
                if(result[m]==result[m+1]):
                    result.pop(m)
                    result.pop(m)
                    answer+=2
                    break
                else:
                    continue
    return answer

