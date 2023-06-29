class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
def bstsum(root,sum):

    if root==None:
        return

    bstsum(root.left,sum)



    sum[0]=sum[0]+root.key

    root.key=sum[0]

    bstsum(root.right,sum)

def inorder(root):

    if root:

        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)

root = Node(9)
root.left = Node(6)
root.right = Node(15)
inorder(root)
sum=[0]
bstsum(root,sum)
print()
inorder(root)