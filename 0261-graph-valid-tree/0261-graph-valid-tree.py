class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        
        if len(edges) != n-1:
            return False

        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node, parent):
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == parent: # undirected graph, dont want to go back to where we started
                    continue

                if neighbor in visited:
                    return False # cycle
                
                # pass current node as parent
                if not dfs(neighbor, node): # if our dfs returns false for nodes neighbors, return False back up
                    return False
            
            return True
        
        # start at 0, mark its neighbor as no one
        if not dfs(0,-1):
            return False
        
        return len(visited) == n # return true only if we visited all the nodes