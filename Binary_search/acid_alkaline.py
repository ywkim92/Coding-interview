def binary_search1(array, n):
    found = False
    first = 0
    last = len(array) - 1
    while first<=last and not found:
        mid = (first+last)//2
        if array[mid]==n: found= True
        elif array[mid]>n: last= mid - 1
        else: first = mid + 1
    return mid, first, last

def binary_search(array, n):
    found = False
    first = 0
    last = len(array) - 1
    while first<=last and not found:
        mid = (first+last)//2
        if array[mid]==n: found= True
        elif array[mid]>n: last= mid - 1
        else: first = mid + 1
    return mid

num, = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
# print(binary_search1([-100, -50, 20, 40, 80], 50))
if len(array)==2: print(*array)
elif array[-1]<0: print(*array[-2:])
elif array[0]>0: print(*array[:2])
else:
  mid = binary_search(array, 0)
  if array[mid]>0:
    pos= array[mid:]
    neg= array[:mid]
  else:
    pos = array[mid+1:]
    neg = array[:mid+1]
  # print(binary_search(array, 2))  
  #print(mid, pos, neg)
  answer = []
  flag = False
  for n in neg:
    opp = binary_search(pos, -n)
    if pos[opp]==-n:
      print(n, -n)
      flag = True
      break
    else:
      if pos[opp]<-n: 
        a, b = opp, opp+1
        if b>=len(pos): b = opp
      else: 
        a, b = opp-1, opp
        if a<0: a=opp
      # print(n, a, b)
      if abs(n+pos[a])<abs(n+pos[b]): 
        answer.append([n, pos[a], abs(n+pos[a])])
      else: answer.append([n, pos[b], abs(n+pos[b])])
  answer = sorted(answer, key =lambda x: (x[2], x[0]), )
  # print(answer)
  if not flag: print(*answer[0][:2])
      
