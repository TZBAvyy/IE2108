# Input 
#   graph: weighted graph as list[dict] where list_index = node, dict[key = node] = distance
# Output
#   msTree: minimum spanning tree
def kruskal(graph:list[dict]):
    sortedByWeight = []
    n = len(graph)
    for node in range(n):
        for vertex, distance in graph[node].items():
            if (vertex, node, distance) not in sortedByWeight:
                sortedByWeight.append((node, vertex, distance))
    sortedByWeight.sort(key=lambda x:x[2])
    disjoint_set = DisjointSet(n)
    msTree = []
    for u, v, weight in sortedByWeight:
        u_set = disjoint_set.find(u)
        v_set = disjoint_set.find(v)
        if u_set != v_set:
            msTree.append((u, v, weight))
            disjoint_set.union(u, v)
    return msTree
    
class DisjointSet:
    def __init__(self, vertices):
        self.parent = [-1]*vertices
    
    def find(self, node):
        if self.parent[node]==-1:
            return node
        return self.find(self.parent[node])
    
    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        if x_set!=y_set:
            self.parent[x_set] = y_set

if __name__ == "__main__":
    # N1 --2-- N5 -3- N4   
    # |      /        \
    # 1    3           4
    # |  /              \
    # N0 --7-- N2 --1-- N3
    graph = [
        {1:1,2:7,5:3},  #Node 0
        {0:1,5:2},      #Node 1
        {0:7,3:1},      #Node 2
        {2:1,4:4},      #Node 3
        {3:4,5:3},      #Node 4
        {0:3,1:2,4:3}   #Node 5
    ]
    print(kruskal(graph))