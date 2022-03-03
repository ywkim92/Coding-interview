'''
2색칠하기
input
9 10
0 1
0 2
0 3
1 5
2 5
3 4
5 6
5 8
6 7
7 8
output
YES
'''
def dfs(start, start_color):
    global graph, colors, flag
    colors[start] = start_color
    
    for x in range(len(graph[start])):
        if colors[graph[start][x]] != 0 and colors[graph[start][x]] == start_color:
            flag = False
            return 
        if colors[graph[start][x]] == 0:
            if colors[start] == 1: dfs(graph[start][x], start_color=-1)
            else: dfs(graph[start][x], start_color=1)
                
                
if __name__=='__main__':
    graph = dict()
    colors = [0]*10000
    flag = True
    
    v, E = map(int, input().split())
    for e in range(E):
        a, b = map(int, input().split())
        try: graph[a].append(b)
        except:
            graph[a] = []
            graph[a].append(b)
            
        try: graph[b].append(a)
        except:
            graph[b] = []
            graph[b].append(a)
    
    dfs(0, 1)
    
    if flag: print('YES')
    else: print('NO')
