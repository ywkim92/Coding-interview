'''
nn단표
input
3
7
output: 6
'''
num, = map(int, input().split())
k, = map(int, input().split())

start = 1
end = num**2

# n보다 작거나 같은 수의 개수?
def getOrder(n):
    tag = 1
    count = 0
    mn = min(num, n)
    while tag<=mn:
        ans = n//tag
        if ans>=num: ans=num
        count+=ans
        tag+=1
    return count

def getMax(n):
    tag = 1
    mn = min(num, n)
    mx = 0
    while tag<=mn:
        ans = n//tag
        if ans>=num: ans=num
        if ans*tag>mx: mx = ans*tag
        tag+=1
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
