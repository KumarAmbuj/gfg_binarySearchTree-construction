class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

def bsttobalancedbst(arr):
    if not arr:
        return

    mid=len(arr)//2

    root=Node(arr[mid])

    root.left=bsttobalancedbst(arr[:mid])
    root.right=bsttobalancedbst(arr[mid+1:])

    return root
def inorder(root,arr):
    if root:
        inorder(root.left,arr)
        arr.append(root.key)
        inorder(root.right,arr)

def printpreorder(root):
    if root:
        print(root.key, end=' ')
        printpreorder(root.left)

        printpreorder(root.right)

root = Node(10)
root.left = Node(8)
root.left.left = Node(7)
root.left.left.left = Node(6)
root.left.left.left.left = Node(5)
arr=[]
inorder(root,arr)
printpreorder(root)
print()
root=bsttobalancedbst(arr)
printpreorder(root)
