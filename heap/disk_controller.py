'''
디스크 컨트롤러(https://programmers.co.kr/learn/courses/30/lessons/42627)
input: [[0, 3], [1, 9], [2, 6]]	
output: 9
input: [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
output: 72
input: [[0,3],[4,4],[5,3],[4,1]]
output: 3
'''
import heapq
# from bisect import bisect_left
def solution(jobs):
    answer=0
    n = len(jobs)
    jobs = sorted(jobs, key = lambda x: (x[0], x[1]))
    prac = 0
    now = 0
    while prac<n:
        start = jobs.pop(0)
        answer+= start[1]
        prac+=1
        now = start[0]+start[1]
        wait = [w[1:]+w for w in jobs if w[0]<=now]
        jobs = [a for a in jobs if a[0]>now]
        heapq.heapify(wait)
        while wait:
            w = heapq.heappop(wait)
            answer += now-w[1]+w[0]
            now+=w[0]
            prac+=1
            push = [p[1:]+p for p in jobs if p[0]<=now]
            jobs = [a for a in jobs if a[0]>now]
            if push:
                for pp in push: heapq.heappush(wait, pp)
    answer//=n
    return answer
