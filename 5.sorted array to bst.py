class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
def arraytobst(arr):

    if not arr:
        return

    mid=len(arr)//2

    root=Node(arr[mid])

    root.left=arraytobst(arr[:mid])
    root.right=arraytobst(arr[mid+1:])

    return root

def inorder(root):

    if root:

        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

arr = [1, 2, 3, 4, 5, 6, 7]
root=arraytobst(arr)
inorder(root)