class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        counter = 0
        nodeMap = defaultdict(list)
        for a, b in edges:
            nodeMap[a].append(b)
            nodeMap[b].append(a)

        visited = set()
        
        def dfs(node):
            # base cases
            if nodeMap[node] == []:
                return True
            
            if node in visited:
                return False

            # if its valid 
            visited.add(node)
            for neighbor in nodeMap[node]:
                dfs(neighbor)
            
            return True
        
        for i in range(n):
            if dfs(i):
                counter += 1

        return counter
            

