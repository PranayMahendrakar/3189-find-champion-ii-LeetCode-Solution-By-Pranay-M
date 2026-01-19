class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Champion has in-degree 0
        # If multiple nodes have in-degree 0, return -1
        # Time: O(n + E), Space: O(n)
        
        in_degree = [0] * n
        
        for u, v in edges:
            in_degree[v] += 1
        
        champion = -1
        for i in range(n):
            if in_degree[i] == 0:
                if champion != -1:
                    return -1  # Multiple champions
                champion = i
        
        return champion