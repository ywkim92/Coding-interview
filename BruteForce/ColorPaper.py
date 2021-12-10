'''example 
input
2
0 0 10 10
2 2 6 6

output
64
36
'''

num, = map(int, input().split())
array = [[0]*101 for _ in range(101)]
papers = []
for _ in range(num):
  papers.append( list(map(int, input().split())) )
  
for i in range(1, num+1):
  x, y, width, height = papers[i-1]
  for r in range(x-1, x-1+width):
    for c in range(y-1, y-1+height):
      array[r][c] = i

for i in range(1, num+1):
  answer = 0
  for r in range(101):
    for c in range(101):
      if array[r][c]==i: answer+=1
  print(answer)
