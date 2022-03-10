## template
def dfs(node, depth, visited):
  global depth_list
  visited[node] = True
  
  for i in range(len(graph[node])):
    if not visited[graph[node][i]]:
      depth_list[graph[node][i]] = depth
      # parents[graph[node][i]] = node
      dfs(graph[node][i], depth+1,  visited)
      
if __name__=='__main__':
  V, x, y = map(int, input().split())
  if V in [0, 1]: print(0)
  else:
    graph = dict()
    # visited = [False]*(V+1)
    depth_list = [0]*1000
    parent = [0]*1000
    for v in range(V-1):
      a, b = map(int, input().split())
      parent[b] = a
      try: graph[a].append(b)
      except:
        graph[a] = []
        graph[a].append(b)
      try: graph[b].append(a)
      except:
        graph[b] = []
        graph[b].append(a)
        
    dfs(0, 1, [False]*1000)
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
    # print(yp)
    # xp = parents[x]
    # yp = parents[y]
    # xps = {xp}
    # yps = {yp}
    # if xp==yp: common = xp
    # else:
    #   while xp!=0:
    #     xp = parents[xp]
    #     xps.add(xp)
    #   while yp!=0:
    #     yp = parents[yp]
    #     yps.add(yp)
    #   cp = xps.intersection(yps)
    #   cp_ = [(c, depth_list[c]) for c in cp]
    #   common = max(cp_, key=lambda x: x[1])[0]
  
    parent_depth = depth_list[yp]
    x_depth = depth_list[x]
    y_depth = depth_list[y]
    # print(parent_depth, x_depth, y_depth)
    if x==y:
      print(0)
    else:
      print(x_depth+y_depth-2*parent_depth)
