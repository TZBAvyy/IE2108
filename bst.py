class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.parent = None
        def __str__(self):
            return f"{self.data}"

    def __init__(self):
        self.root = None

    def insert(self, data): #RETURNS NONE
        newNode = self.Node(data)
        if self.root==None:
            self.root = newNode
        else:
            self._insertRecurs(self.root, newNode)

    def _insertRecurs(self, root, newNode):
        if newNode.data < root.data:
            if root.left == None:
                root.left = newNode
                newNode.parent = root
            else:
                self._insertRecurs(root.left, newNode)
        else:
            if root.right == None:
                root.right = newNode
                newNode.parent = root
            else:
                self._insertRecurs(root.right, newNode)

    def find(self, data): #RETURNS Node object where Node.data == data OR None if no Node object has data
        ref = self.root
        while ref!=None and ref.data!=data:
            if data < ref.data:
                ref = ref.left
            else:
                ref = ref.right
        return ref

    def delete(self, data): #RETURNS True if data is deleted else False if data not found
        ref = self.find(data)
        if ref==None:
            return False #No node with that data
        
        if (ref.left==None or ref.right==None): # Case of 1 or 0 child in ref
            self.replace(ref)
            return True
        #Find leftmost node in ref.right subtree (minimum value on the right)
        succ = ref.right
        while succ.left!=None:
            succ = succ.left 
        #Move successor up to reference
        ref.data = succ.data
        #Delete succ (succ must only have 1 or 0 child since it is leftmost node)
        self.replace(succ)
        return True
    
    #For the case ref has one or no child (no 2 childs)
    def replace(self, ref):
        if ref.left == None:
            child = ref.right #Child is on ref.right or is None
        else:
            child = ref.left #Child is on ref.left

        if ref.parent.left == ref:
            # Ref is on root.left
            ref.parent.left = child
        else: 
            # Ref is on root.right
            ref.parent.right = child
        if child != None:
            child.parent = ref.parent #Change child parent to root
        if ref.parent == None:
            self.root = child #Case of self.root to be deleted
        
    def print(self):
        self._inorder(self.root, 0, "")

    def _inorder(self, root, height, path):
        if root!=None:
            self._inorder(root.left, height+1, "/")
            print(f'{path} {root}'.rjust(height*8))
            self._inorder(root.right, height+1, "\\")


b = BST()
b.insert(14)
b.insert(10)
b.insert(12)
b.insert(20)
b.insert(11)
b.insert(15)
b.insert(40)
b.insert(7)
b.insert(1)
b.insert(100)
b.insert(9)
b.print()
print("DELETING 10 NOW")
b.delete(10)
b.print()
print("DELETING 14 NOW")
b.delete(14)
b.print()
print("DELETING 100 NOW")
b.delete(100)
b.print()
print("DELETING 7 NOW")
b.delete(7)
b.print()