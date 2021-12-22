'''
삼각 달팽이(https://programmers.co.kr/learn/courses/30/lessons/68645)
input, output
4, [1,2,9,3,10,8,4,5,6,7]
5, [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
6, [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
'''
def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    limit = n*(n+1)//2
    count = 0
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    nx, ny = 0,0
    d = 0
    while count<limit:
        count+=1
        answer[nx][ny] = count
        x = nx+dx[d]
        y = ny+dy[d]
        if not (0<=x<n and 0<=y<n):
            d = (d+1)%3
            nx+=dx[d]
            ny+=dy[d]
        elif answer[x][y]==0:
            nx+=dx[d]
            ny+=dy[d]
        else:
            d = (d+1)%3
            nx+=dx[d]
            ny+=dy[d]

    ans = []
    for a in answer: ans+=a
    return ans
