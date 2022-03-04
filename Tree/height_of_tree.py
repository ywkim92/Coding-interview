'''
input
8 0
0 1
0 2
1 3
1 4
1 5
2 6
6 7
output
3
'''
def dfs(node, depth, visited):
  global depth_list
  visited[node] = True
  
  for i in range(len(graph[node])):
    if not visited[graph[node][i]]:
      depth_list[graph[node][i]] = depth
      dfs(graph[node][i], depth+1,  visited)
      
if __name__=='__main__':
  V, start = map(int, input().split())
  graph = dict()
  # visited = [False]*(V+1)
  depth_list = [0]*V
  for v in range(V-1):
    a, b = map(int, input().split())
    try: graph[a].append(b)
    except:
      graph[a] = []
      graph[a].append(b)
    
    try: graph[b].append(a)
    except:
      graph[b] = []
      graph[b].append(a)
  if V==1:
    print(0)
  else:
    dfs(start, 1, [False]*(V))
    print(max(depth_list))
