"""
dfs and bfs in graphs
"""

# graph in adjacency list
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'F'},
    'C': {'A', 'F'},
    'D': {'B',},
    'E': {'B', 'F'},
    'F': {'C', 'E'}         
}

# DFS algorithm
def dfs(graph, start, visited=None):
    # cria o set dos visitados caso não tenha sido criado
    if visited is None:
        visited = set()
        
    visited.add(start)

    print(start)

    # para cada node adjascente que não tenha sido visitado ainda (graph[start] - visited)
    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited

dfs(graph, 'A')