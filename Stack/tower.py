'''
input
5
6 9 5 7 4
output: 0 0 2 2 4
'''
num, = map(int, input().split())
array = list(map(int, input().split()))
stack = []
answer = [0 for _ in range(num)]

for n in range(num):
  while stack:
    if stack[-1][1]>=array[n]:
      answer[n]= stack[-1][0]+1
      break
    else: stack.pop()
  stack.append([n, array[n]])
  
print(*answer)
