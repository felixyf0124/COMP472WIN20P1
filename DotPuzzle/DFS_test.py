# import sys
# sys.path.append("..")

import unittest


# print(sys.path)
import DFS as df

class TestDFS(unittest.TestCase):
    
    def test_addRoot(self):
        dfs = df.DFS(8)
        rootState = "111000101"
        dfs.addRoot(rootState)
        self.assertEqual(len(dfs.openList), 1)
        self.assertEqual(dfs.openList[0],rootState)
        self.assertEqual(len(dfs.solution), 1)
        self.assertEqual(dfs.solution[0][0],"0")
        self.assertEqual(dfs.solution[0][1],rootState)


if __name__ == '__main__':
    unittest.main()