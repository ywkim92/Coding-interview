length, n_orders = map(int, input().split())
array = [0 for _ in range(length)]
front = 0
rear = 0

for _ in range(n_orders):
  ''' operation directions
  push: like 1 4, push 4
  pop: 2
  print top: 3
  '''
  order= list(map(int, input().split()))
  if order[0]==1:
    if rear==length: print('Overflow')
    else:
      array[rear] =order[1] 
      rear+=1 
  elif order[0]==2:
    if front==rear: print('Underflow')
    else:
      array[front]=0
      front+=1 
  else: 
    if front==rear: print('NULL')
    else: print(array[front])
