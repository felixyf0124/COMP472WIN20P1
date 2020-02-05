
class Loader:
    def __init__(self, path):
        self.myPuzzleList = []
        file = open(path, "r")
        # for line in file:
            # m = line.match(r"\d+ \d+ \d+ \d+",4)