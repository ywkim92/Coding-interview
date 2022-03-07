'''
네트워크(https://programmers.co.kr/learn/courses/30/lessons/43162)
'''
def dfs(graph, start, visited = []):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

def solution(n, computers):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j: continue
            else:
                if computers[i][j] ==0:
                    continue
                else:
                    graph[i].append(j)
                    graph[j].append(i)
    answer = 1
    comp_set = set(range(n))
    subset = set(dfs(graph, 0, []))
    not_inc = comp_set - subset
    if not not_inc: return answer
    elif len(not_inc)==1: return answer+1
    else:
        n_subset = len(not_inc)
        new = list(not_inc)[0]
        while n_subset!=0:
            ss = dfs(graph, new, [])
            not_inc -= set(ss)
            n_subset = len(not_inc)
            answer +=1
            if n_subset==0:
                return answer
            new = list(not_inc)[0]
