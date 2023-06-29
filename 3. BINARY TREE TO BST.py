class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
def inorder(root,list):
    if root:
        inorder(root.left,list)
        list.append(root.key)
        inorder(root.right,list)
    else:
        return

def binarytobst(root,list):
    if root:
        binarytobst(root.left,list)
        root.key=list[0]
        list.pop(0)
        binarytobst(root.right,list)
def display(root):
    if root:
        display(root.left)
        print(root.key,end=' ')
        display(root.right)
def partition(arr,p,r):
    x=arr[r]

    i=p-1

    for j in range(p,r):
        if arr[j]<=x:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1
def quicksort(arr,p,r):
    if p<r:

        q=partition(arr,p,r)

        quicksort(arr,p,q-1)
        quicksort(arr,q+1,r)


root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right= Node(5)
list=[]
inorder(root,list)
print(list)
quicksort(list,0,len(list)-1)
print(list)
binarytobst(root,list)
display(root)