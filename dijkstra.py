# Input: 
#       Graph: weighted graph in form of list of dictionary with 
#       Start: node to start from in form of int
# Output: 
#       Shortest Path List: list of int where list[node_start] = shortest distance to node_end from node_start
def dijkstra(graph:list[dict], start:int):
    queue = [start]
    visited = []
    shortestPath = [float('inf')]*len(graph)
    shortestPath[start] = 0

    while queue:
        vertex = queue.pop(0)
        visited.append(vertex)
        for neighbor, neighborDistance in graph[vertex].items():
            if neighbor not in visited:
                shortestPath[neighbor] = min(shortestPath[neighbor],                   # Another Path from start to neighbor / Infinity if no path yet
                                             shortestPath[vertex] + neighborDistance) # Distance from start to vertex + Distance from vertex to neightbor
                queue.append(neighbor)
    return shortestPath

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
    print(dijkstra(graph,0))
    print(dijkstra(graph,3))
    print(dijkstra(graph,5))