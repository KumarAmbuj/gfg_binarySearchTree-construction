class newNode:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

def bsttosum(root,sum):

    if root:
        bsttosum(root.right, sum)

        sum[0] = sum[0] + root.key

        root.key = sum[0] - root.key

        bsttosum(root.left, sum)


def inorder(root):
    if root:

        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)


root = newNode(11)
root.left = newNode(2)
root.right = newNode(29)
root.left.left = newNode(1)
root.left.right = newNode(7)
root.right.left = newNode(15)
root.right.right = newNode(40)
root.right.right.left = newNode(35)
sum=[0]
inorder(root)
print()
bsttosum(root,sum)
inorder(root)
