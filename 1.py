'''def linearSearch(array,n,x):
    for i in range(0,n):
        if (array[i]==x):
            return i
    return -1
array=[2,4,0,1,9]
x=9
n=len(array)
result=linearSearch(array,n,x)
if (result==-1):
    print("Element not found")
else:
    print("Element found at index:",result)'''



'''def binarySearch(array,x,low,high):
    while low<=high:
        mid=low+(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
array=[3,4,5,6,7,8,9]
x=8
result=binarySearch(array,x,0,len(array)-1) 
if result !=-1:
    print("Element is preent at index"+str(result))
else:
    print("Element not found")'''



'''class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val)+"->",end='')
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val)+"->",end='')
def preorder(root):
    if root:
        print(str(root.val)+"->",end='')
        preorder(root.left)
        preorder(root.right)
root=Node(1)
root.left =Node(2)
root.right =Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("\nInorder")
inorder(root)
print("\npreorder")
preorder(root)
print("\npostorder")
postorder(root)'''



'''class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key)+"->",end='')
        inorder(root.right)
def minValueNode(node):
    current=node
    while(current.left is not None):
        current=current.left
    return current
def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def deleteNode(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left=deleteNode(root.left,key)
    elif(key > root.key):
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minValueNode(root.righ)
        root.key=temp.key
root=None
root=insert(root,8)
root=insert(root,3)
root=insert(root,1)
root=insert(root,6)
root=insert(root,7)
root=insert(root,10)
root=insert(root,14)
root=insert(root,4)
print("Inorder traversal:",end='')
inorder(root)
print("\nDelete 10")
root=deleteNode(root,10)
inorder(root)'''



def find_unknown_words(text, vocabulary):
    words = text.split()
    vocab_set = set(vocabulary)
    unknown_words = set()
    for word in words:
        if word not in vocab_set:
            unknown_words.add(word)
    if not unknown_words:
        return -1
    else:
        return unknown_words
text = "the sun rises in the east"
vocabulary = ["sun", "in", "east", "doctor", "day"]
unknown_words = find_unknown_words(text, vocabulary)
print(unknown_words)
