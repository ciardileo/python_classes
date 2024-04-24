"""
Exercícios sobre DFS e BFS em grafos
"""

# Ex 01 - dfs de um grafo comum

# friends = {
#     'alice': {'carlos'},
#     'carlos': {'bob', 'alice'},
#     'bob': {'carlos'},
#     'david': {'ellen'},
#     'ellen': {'david'}
# }

# # complexidade = O(5 + 3 = 8)
# def dfs_friends(graph, start, visited=None):
#     # initialize the visited set
#     if visited == None:
#         visited = set(start)
        
#     visited.add(start)
#     print(start)
    
#     # for each adjacente friend that is not in visited
#     for friend in graph[start] - visited:
#         dfs_friends(graph, friend, visited)
    
#     return visited

# print("DFS Friends:")
# start = input('Start: ').strip().lower()
# target = input('Target: ').strip().lower()

# result = dfs_friends(friends, start)

# if target in result:
#     print(f"There is a connection between {start} and {target}.")
# else:
#     print(f"There isn't a connection between {start} and {target}.")
   
# print('-' * 25) 
    
# Ex 02 - dfs de um grafo direcionado

cities = {
    'sp': {'rj'},
    'rj': {'sp', 'es'},
    'es': set(),
    'mt': set(),
    'mg': {'es', 'mt', 'sp'}
}

# complexidade = O(5 + 3 = 8)
def dfs_cities(graph, start, target, visited=None):
    # initialize the visited set
    if visited == None:
        visited = set(start)
        
    visited.add(start)
    
    if target in visited and start == target:
        print(f'{start} X')
    elif target not in visited:
        print(f'{start} ->', end=' ')
    
    
    
    # for each adjacente friend that is not in visited
    for city in graph[start] - visited:
        dfs_cities(graph, city, target, visited)
    
    print()
    return visited

print("DFS City:")
start = input('Start: ').strip().lower()
target = input('Target: ').strip().lower()

result = dfs_cities(cities, start, target)

if target in result:
    print(f"There is a connection between {start} and {target}.")
else:
    print(f"There isn't a connection between {start} and {target}.")