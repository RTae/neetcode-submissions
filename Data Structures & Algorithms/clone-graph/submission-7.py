"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = {}

        def dfs(node):
            # if this node already visit in gragh data just return its neighbors
            if node in graph:
                return graph[node]

            # Copy data
            copy = Node(node.val)
            graph[node] = copy

            # check node neighbors
            for nei in node.neighbors:
                # Loop create with dfs in each neighbors
                copy.neighbors.append(dfs(nei))
            
            # return new node
            return copy

        return dfs(node) if node else None 