class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

def levelorder(root,data):
    if root==None:
        root=Node(data)
        return root

    if data<root.key:
        root.left=levelorder(root.left,data)
    else:
        root.right=levelorder(root.right,data)

    return root

def constructbst(arr,n):
    if n==0:
        return None

    root=None

    for i in range(len(arr)):
      root =  levelorder(root,arr[i])

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)

arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]

root=constructbst(arr,len(arr))
inorder(root)
