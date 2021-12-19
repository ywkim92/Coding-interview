# num: the number of nodes
# x, y: two nodes that need to find the lowest common ancestor
num, x, y = map(int, input().split())
parent = [0]*num
for _ in range(num-1):
  a, b = map(int, input().split())
  parent[b] = a 

xp = parent[x]
xs = [xp]
while xp!=0:
  xp = parent[xp]
  xs.append(xp)
  
yp = parent[y]
ys = [yp]
found = False
while not found:
  if yp in xs: found = True
  else:
    yp = parent[yp]
print(yp)
