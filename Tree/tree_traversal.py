num, = map(int, input().split())
tree = [[] for _ in range(num)]

for _ in range(num):
  a, b, c = map(int, input().split())
  tree[a] = [b, c]
# ------------------------------------
def preorder(n):
  if tree[n][0]==-1 and tree[n][1]==-1: print(n, end=' ')
  else:
    print(n, end=' ')
    if tree[n][0]!=-1: preorder(tree[n][0])
    if tree[n][1]!=-1: preorder(tree[n][1])

def inorder(n):
  if tree[n][0]==-1 and tree[n][1]==-1: print(n, end=' ')
  else:
    if tree[n][0]!=-1: inorder(tree[n][0])
    print(n, end=' ')
    if tree[n][1]!=-1: inorder(tree[n][1])

def postorder(n):
  if tree[n][0]==-1 and tree[n][1]==-1: print(n, end=' ')
  else:
    if tree[n][0]!=-1: postorder(tree[n][0])
    if tree[n][1]!=-1: postorder(tree[n][1])
    print(n, end=' ')
  
preorder(0)
inorder(0)
postorder(0)
