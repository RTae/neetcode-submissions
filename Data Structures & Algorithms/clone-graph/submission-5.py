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
        
        # Contrust graph by using dfs
        def dfs(node):
            # if this node already in graph just return in neighbors
            if node in graph:
                return graph[node]

            # Create a copy
            copy = Node(node.val)
            graph[node] = copy
            
            # Loop create each neighbors
            for nei in node.neighbors:
                # append into new copy while dfs copy
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node) if node else None