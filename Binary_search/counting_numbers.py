'''
숫자 개수 세기
input
10 4
1 3 4 3 2 3 1 2 5 10
1 3 9 10
output
2
3
0
1
'''
n, q = map(int, input().split())
array = list(map(int, input().split()))
query = list(map(int, input().split()))

array.sort()

def bs(array, n):
  ind = -1
  start = 0
  end = len(array)-1
  while start<=end and (ind==-1):
    mid = (start+end)//2
    if array[mid]==n: ind=mid
    elif array[mid]>n: end = mid -1
    else: start = mid +1
  return ind
  
for q in query:
  q_ind = bs(array, q)
  if q_ind==-1: print(0)
  else:
    count=0
    ind_origin = q_ind
    ind = ind_origin
    while ind<n:
      if array[ind]==q:
        count+=1 
        ind+=1
      else: break
    ind = ind_origin-1
    while ind>-1:
      if array[ind]==q:
        count+=1
        ind-=1
      else: break
    print(count)
