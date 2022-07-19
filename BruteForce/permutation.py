'''
example input
4 2
example output
ab
ac
ad
ba
bc
bd
ca
cb
cd
da
db
dc
'''

n, r = map(int, input().split())
def solution(): 
  picked = [] 
  def recur(): 
    temp = ''
    if len(picked) == r: 
      for j in range(r):
        temp += chr(picked[j]+ord('a'))
      print(temp)
      return 
      
    for i in range(n): 
      if i not in picked: 
        picked.append(i)
        recur() 
        picked.pop() 
          
  recur() 
  
solution()
