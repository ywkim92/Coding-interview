'''
더 맵게(https://programmers.co.kr/learn/courses/30/lessons/42626)
'''
import heapq
def solution(scoville, K):
    answer = 0
    #s = scoville.copy()
    n = len(scoville)
    heapq.heapify(scoville)
    while 1:
        a = heapq.heappop(scoville)
        if a>=K:
            return answer
        else:
            b= heapq.heappop(scoville)
            heapq.heappush(scoville, a+b*2)
            answer+=1
        if answer==n-1:
            break
    if scoville[0]<K:
        return -1
    else:
        return answer
