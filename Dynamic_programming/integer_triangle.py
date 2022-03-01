'''
정수 삼각형(https://programmers.co.kr/learn/courses/30/lessons/43105)
'''
def solution(triangle):
    answer = 0
    n = len(triangle)
    for i in range(1, n):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][-1] += triangle[i-1][-1]
        for j in range(1, i):
            triangle[i][j] += max(triangle[i-1][j-1:j+1])
    return max(triangle[n-1])
