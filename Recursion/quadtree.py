'''
쿼드압축 후 개수 세기(https://programmers.co.kr/learn/courses/30/lessons/68936)
input
[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
output
[4,9]
'''
import numpy as np
count = [0,0]
def solution(arr):
    array1 = np.array(arr, dtype=np.int64)
    global count
    def sol(array, ):
        n = len(array)//2
        if array.size==1:
            if array[0,0]==0: count[0]+=1
            else: count[1]+=1
            return 
        elif len(np.unique(array))==1:
            if array[0,0]==0: count[0]+=1
            else: count[1]+=1
            return 
        else:
            sol(array[:n,:n], )
            sol(array[:n,n:], )
            sol(array[n:,:n], )
            sol(array[n:,n:], )
            return count
    sol(array1)
    return count
