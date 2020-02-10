class DFSearch:
    def __init__(self, max_d):
        self.closedList = []
        self.openList = []
        self.visited = []
        self.solution = []
        self.current_d = 0
        self.max_d = max_d
        # Using a Python dictionary to act as an adjacency list
        self.graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': [],
            'F': []
        }

    # node: move, state
    def doSearch(self, depth, node):
        if node not in self.visited:
            print(node)
            self.visited.append(node)
            self.solution.append(node)
            if self.current_d < self.max_d:
                for neighbour in self.graph[node]:
                    depth += 1
                    print(depth)
                    self.doSearch(depth, neighbour)
            # else:
            #     # touch(SAME)
            #     self.solution.pop()
            #     doSearch(visited, neighbour)


# loader = ld.Loader("path.txt")
#
# dotP = dp.DotPuzzle(3)
# dotP.import1DState(loader.getMyPuzzleAt(0))

# dotP.touch("A",1)
# 1dStr = dotP.get1DState()
