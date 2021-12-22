'''
중복 없는 구간
input
10
1 3 1 2 4 2 1 3 2 1
output: 4
input
7
7 1 4 2 5 3 6
output: 7
'''
num, = map(int, input().split())
array = list(map(int, input().split()))

def check(arr, k):
    iters = len(arr)-k+1
    count = [0]*100001
    dup = 0
    for i in range(iters):
        if i==0:
            ar = arr[:k]
            for a in ar:
                if count[a]>0:dup+=1
                count[a]+=1
        else:
            if count[arr[i-1]]>1: dup-=1
            count[arr[i-1]]-=1
            if count[arr[i+k-1]]>=1: dup+=1
            count[arr[i+k-1]]+=1
        if dup==0: return True
    return False
    
start = 1
end = num
found = False
if check(array, end):
  print(end)
  found = True
while end-start>1 and not found:
    mid = (start+end)//2
    poss = check(array, mid)
    if not poss: end = mid
    else: start=mid
if not found: print(start, )
