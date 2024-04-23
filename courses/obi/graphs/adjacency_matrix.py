"""
estudo de grafos
"""

# connected, non-directed graph
class Graph:
    # crete a adjacency matrix
    def __init__(self, size):
        self.matrix = [[0] * size for i in range(size)]
        self.size = size

    # add edge
    def add_edge(self, v1, v2):
        if v1 == v2:
            print(f"Same vertex {v1} and {v2}")
            return
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1

    # remove edge
    def remove_edge(self, v1, v2):
        if self.matrix[v1][v2] == 0:
            print(f"No edge between {v1} and {v2}")
            return
        self.matrix[v1][v2] = 0
        self.matrix[v2][v1] = 0

    # to be able to len(graph)
    def __len__(self):
        return self.size

    # print
    def print_matrix(self):
        print(*self.matrix, sep='\n')


if __name__ == '__main__':
    
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()