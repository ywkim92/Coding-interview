'''
* input
bacd
* output
push
push
pop
pop
push
pop
push
pop
'''

string = input()
ln = len(string)
inputs = list(string)
inputs.sort()

inp = inputs.pop(0)
stack = [inp]
result = [1,]
answer = ''
tag = 0
flag = False
for _ in range(1, 2*ln):
  if not stack:
    inp = inputs.pop(0)
    stack.append(inp)
    result.append(1)
    continue
  if stack[-1]==string[tag]:
    p = stack.pop()
    answer+=p
    tag+=1 
    result.append(-1)
  else:
    if string[tag] in stack[:-1]:
      print('impossible')
      flag  =True
      break
    else:
      inp = inputs.pop(0)
      stack.append(inp)
      result.append(1)
if not flag:
  for r in result:
    if r==1: print('push')
    else: print('pop')
    
