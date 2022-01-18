'''
input: 5
output
4+1
3+2
3+1+1
2+2+1
2+1+1+1
1+1+1+1+1
6
'''
num, =map(int, input().split())
def pick(n, picked, to_pick=0):
    global counts
    if to_pick >= n:
        if to_pick==n:
            #ans = picked.copy()
            print('+'.join([str(i) for i in picked]))
            counts+=1
            # result.append(ans)
            return
        else: return 
    
    if not picked:
        smallest = n-1
    else:
        smallest = picked[-1]
    
    for _next in range(smallest, 0,-1):
        picked.append(_next)
        pick(n, picked, to_pick+_next)
        picked.pop()
        
counts = 0
pick(num, [], )
print(counts)
