'''
입국심사(https://programmers.co.kr/learn/courses/30/lessons/43238)
input: 6, [7,10]
output: 28
'''
def getPoss(n, times, total):
    mans = sum(total//t for t in times)
    if mans>=n: return True
    else: return False
def solution(n, times):
    answer = 0
    start = 0
    end = max(times)*n
    while end-start>1:
        mid = (start+end)//2
        poss = getPoss(n,times, mid)
        if poss: end=mid
        else: start = mid
    return end
