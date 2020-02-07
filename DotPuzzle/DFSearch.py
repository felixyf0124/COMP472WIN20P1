
class DFSearch:
    def __init__(self, max_d):
        self.closedList = []
        self.openList = []
        self.current_d = 0
        self.max_d = max_d
