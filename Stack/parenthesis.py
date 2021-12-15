'''
intput: (()[[]])([])
output: 28
input: (()()[]
output: 0
'''

ps = input()
pslist = list(ps)
length = len(ps)
dic = dict(zip(['(', '[',], [')', ']',]))
opp = dict(zip(['(', '[',], [']',')', ]))
stack = []

for l in range(length):
    if not stack:
        p = pslist.pop(0)
        stack.append(p)
        if p in dic.values():
          break
    else:
        p = pslist.pop(0)
        # when the top of stack is an open bracket ( or [
        if stack[-1] in dic:
            # when the top is corresponding with the input p, like '(' and ')'
            if dic[stack[-1]]==p:
                stack.pop()
                if p==']': stack.append(3)
                else: stack.append(2)
                try:
                    if type(stack[-2]) == int and type(stack[-1])==int:
                        i = stack.pop()
                        j = stack.pop()
                        stack.append(i+j)
                except: pass
            # when the top isn't corresponding with the input p, like '(' and ']'
            elif p == opp[stack[-1]]: break 
            else:
                stack.append(p)
        # when the top of stack is an integer
        else:
            # when the input p is an open bracket
            if p in dic:
                stack.append(p)
            else:
                # like '()]'
                if len(stack)==1:
                    stack.append(p)
                    break
                # like '[()]'
                elif dic[stack[-2]]==p:
                    integer = stack.pop()
                    stack.pop()
                    if p==']': stack.append(3*integer)
                    else: stack.append(2*integer)
                    try:
                        if type(stack[-2]) == int and type(stack[-1])==int:
                            i = stack.pop()
                            j = stack.pop()
                            stack.append(i+j)
                    except: pass
                # like '[())'
                else: break
    # print(stack)
if len(stack)>1: print(0)
else:
    if type(stack[0]) ==int: print(*stack)
    else: print(0)
