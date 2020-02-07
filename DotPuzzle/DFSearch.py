
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
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # Array to keep track of visited nodes.


def dfs(visited, graph, node):
    MAX_DEPTH = 3
    depth = 0
    if node not in visited:
        print(str(node))
        print(depth)
        visited.append(node)
        depth += 1
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
dfs(visited, graph, 'A')
