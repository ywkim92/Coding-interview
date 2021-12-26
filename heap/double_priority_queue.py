'''
이중우선순위큐(https://programmers.co.kr/learn/courses/30/lessons/42628)
'''
import heapq
def solution(operations):
    ans = []
    num = len(operations)
    for n in range(num):
        a, b = operations[n].split()
        if a=='I': 
            heapq.heappush(ans, int(b))
        else:
            if not ans: continue
            elif int(b)==-1:
                heapq.heappop(ans)
            else:
                if len(ans)==1:
                    heapq.heappop(ans)
                else:
                    mn = heapq.heappop(ans)
                    ans = ans[:-1]
                    heapq.heappush(ans,mn)
    if not ans: return [0,0]
    elif len(ans)==1: return [ans[0],ans[0]]
    else:
        return [max(ans), min(ans) ]
