'''구간의 합집합
input
2
1 4
3 5
3
output
3
input
3
1 3
2 10
1 8
5
output
3
'''
num, = map(int, input().split())
array= []
start = 1
end = 0
for _ in range(num):
    array.append(list(map(int, input().split())))
    if array[-1][1]> end: end = array[-1][1]
k, = map(int, input().split()) 
k+=1

# n보다 작거나 같은 수의 개수?
def getOrder(n):
    count = 0
    for s, e in array:
        if e < n: count+=(e-s+1)
        elif s > n: count+=0
        else: count+=n-s+1 
    return count

def getMax(n):
    mx = 0
    for s, e in array:
        if e < n: ans = e
        else: ans =n
        if ans>mx: mx=ans
    return mx

found = False
while start<=end and not found:
    mid = (start+end)//2
    go = getOrder(mid)
    if go==k:
        print(getMax(mid))
        found = True
    else:
        if go>k: end = mid - 1
        else: start = mid +1
if not found: print(getMax(start))
