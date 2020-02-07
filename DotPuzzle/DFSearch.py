# class DFSearch:
#     def __init__(self, max_d):
#         self.closedList = []
#         self.openList = []
#         self.current_d = 1
#         self.max_d = max_d

# Using a Python dictionary to act as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # Array to keep track of visited nodes.
MAX_DEPTH = 3
depth = 0


def dfs(visited, graph, node, depth):
    if node not in visited:
        print(str(node))
        visited.append(node)
        for neighbour in graph[node]:
            depth += 1
            print(depth)
            dfs(visited, graph, neighbour, depth)


# Driver Code
dfs(visited, graph, 'A', depth)
