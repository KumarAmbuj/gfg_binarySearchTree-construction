class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
def getpreindex():
    return constructTreeUtil.preindex
def increment():
    constructTreeUtil.preindex+=1

def constructTreeUtil(pre, low, high, size):

    if (getpreindex() >= size or low > high):
        return None


    root = Node(pre[getpreindex()])
    increment()


    if low == high:
        return root


    for i in range(low, high + 1):
        if (pre[i] > root.key):
            break


    root.left = constructTreeUtil(pre, getpreindex(), i - 1, size)

    root.right = constructTreeUtil(pre, i, high, size)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)

def constructTree(pre):
    size=len(pre)
    constructTreeUtil.preindex=0
    return constructTreeUtil(pre,0,size-1,size)
pre = [10, 5, 1, 7, 40, 50]
root=constructTree(pre)
inorder(root)

