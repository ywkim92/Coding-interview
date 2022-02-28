'''
주식가격(https://programmers.co.kr/learn/courses/30/lessons/42584)
'''
def solution(prices):
    answer = []
    n = len(prices)
    check=0
    for check in range(n):
        count = check
        while prices[check]<=prices[count]:
            
            if count>=n-1:
                break
            count+=1
        answer.append(count-check)
    return answer
