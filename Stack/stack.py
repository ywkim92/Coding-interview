length, opers = map(int, input().split())
array = []
for _ in range(opers):
  order = list(map(int, input().split()))
  # print(order)
  if order[0]==1:
    if len(array)==length: print('Overflow')
    else: array.append(order[1])
  elif order[0]==2:
    if len(array)==0: print('Underflow')
    else: array.pop()
  else:
    if len(array)==0: print('NULL')
    else: print(array[-1])
