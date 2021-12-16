'''
length: length of queue
n_orders: the number of operations
max_len: maximum length of queue
'''
length, n_orders, max_len = map(int, input().split())
array = [0]*length
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
    if rear==max_len: print('Overflow')
    else:
      array[rear] =order[1] 
      if rear>=length-1: rear = 0
      else: rear+=1 
      if rear==front: rear=max_len
  elif order[0]==2:
    if front==rear: print('Underflow')
    else:
      array[front]=0
      if rear==max_len: rear=front
      if front>=length-1: front = 0
      else: front+=1
  else: 
    if front==rear: print('NULL')
    else: print(array[front])
