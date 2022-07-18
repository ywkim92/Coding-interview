num, = map(int, input().split())

def seq(n):
  return 1 + sum(range(6, 6*(n-1)+1, 6))
  
i = 1 
limit = seq(i)
while num > limit:
  i+=1 
  limit = seq(i)
print(i)
