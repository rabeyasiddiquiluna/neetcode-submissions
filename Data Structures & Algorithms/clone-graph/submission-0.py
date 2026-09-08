"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node1):
            if  node1 in oldToNew:
                return oldToNew[node1]
            
            copy = Node(node1.val)
            oldToNew[node1] = copy

            for nei in node1.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None


        