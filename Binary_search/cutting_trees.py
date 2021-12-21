num, m = map(int, input().split())
array = list(map(int, input().split()))

def ln(array, n):
    result = 0
    for a in array:
        if a-n>0: result+=(a-n)
    return result

start = 1
end = max(array)
found = False

while end-start>1 and not found:
    mid = (start+end)//2
    gain = ln(array, mid)
    if m > gain: end = mid
    else: start=mid
if not found: print(start, )
