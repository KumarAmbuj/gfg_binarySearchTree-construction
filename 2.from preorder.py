INT_MIN = float("-infinity")
INT_MAX = float("infinity")

class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

def getpreindex():
    return constructTreeUtil.preindex

def increment():
    constructTreeUtil.preindex+=1

def constructTreeUtil(pre,key,mini,maxi,size):

    if getpreindex()>=size:
        return None

    if key >mini and key < maxi:

        root=Node(key)

        increment()

        if getpreindex()<size:

            root.left=constructTreeUtil(pre,pre[getpreindex()],mini,key,size)
            root.right=constructTreeUtil(pre,pre[getpreindex()],key,maxi,size)

    return root


def constructTree(pre):
    constructTreeUtil.preindex = 0
    size = len(pre)
    return constructTreeUtil(pre, pre[0], INT_MIN, INT_MAX, size)


def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.key)
    printInorder(node.right)
pre = [10, 5, 1, 7, 40, 50]
root = constructTree(pre)

printInorder(root)

