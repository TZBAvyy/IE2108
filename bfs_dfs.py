from bst import BST

#Input: tree: binary tree of nodes with tree.root being the starting node and each node has .left and .right, 
#       data: data of node to be found
#Output: Node where Node.data == input_data + visited list (traversal path)
def bfSearch(tree:BST, data:int):
    visited = []
    queue = [tree.root]

    while queue:
        vertex = queue.pop(0)
        visited.append(vertex)

        if vertex.data == data:
            return vertex, visited
        
        if vertex.left != None and vertex.left not in visited:
            queue.append(vertex.left)

        if vertex.right != None and vertex.right not in visited:
            queue.append(vertex.right)
    return None, visited

#Input: tree: binary tree of nodes with tree.root being the starting node and each node has .left and .right, 
#       data: data of node to be found
#Output: Node where Node.data == input_data + visited list (traversal path)
def dfSearch(tree:BST, data:int):
    visited = []
    stack = [tree.root]

    while stack:
        vertex = stack.pop()
        visited.append(vertex)

        if vertex.data == data:
            return vertex, visited
        
        if vertex.left != None and vertex.left not in visited:
            stack.append(vertex.left)

        if vertex.right != None and vertex.right not in visited:
            stack.append(vertex.right)
    return None, visited

if __name__ == "__main__":
    b = BST.create_Instance(3)   

    node, lst = bfSearch(b, None)
    for i in lst:
        print(f"{i}", end=", ")

    print()

    node2, lst2 = dfSearch(b, None)
    for i in lst2:
        print(f"{i}", end=", ")

    print()