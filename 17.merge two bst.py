class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

def inorder(root,arr):
    if root:
        inorder(root.left,arr)
        arr.append(root.key)
        inorder(root.right,arr)
def merge(arr1,arr2):
    n = len(arr1) + len(arr2)
    arr1.append(2345)
    arr2.append(2345)
    arr=[]

    i=0
    j=0
    for k in range(n):
        if arr1[i]<=arr2[j]:
            arr.append(arr1[i])
            i=i+1
        else:
            arr.append(arr2[j])
            j=j+1

    return arr
def constructbst(arr):
    if not arr:
        return

    mid=len(arr)//2

    root=Node(arr[mid])

    root.left=constructbst(arr[:mid])
    root.right=constructbst(arr[mid+1:])
    return root
def display(root):
    if root:
        display(root.left)
        print(root.key,end=' ')
        display(root.right)


root = Node(100)
root.left = Node(50)
root.right = Node(300)
root.left.left = Node(20)
root.left.right = Node(70)

display(root)
print()

root2=Node(80)
root2.left=Node(40)
root2.right=Node(120)
display(root2)
print()

arr1=[]
inorder(root,arr1)
arr2=[]
inorder(root2,arr2)

print(arr1)
print(arr2)

arr=merge(arr1,arr2)
print(arr)

root=constructbst(arr)
display(root)
