class Solution(object):
    res = 0

    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = dict()
        for n1, n2 in edges:
            if n1 not in graph:
                graph[n1] = set()
            if n2 not in graph:
                graph[n2] = set()
            graph[n1].add(n2)
            graph[n2].add(n1)
        visited = set()
        self.dfs(visited, graph, 0)
        return self.res

    def dfs(self, visited, graph, node):
        max1, max2 = 0, 0
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                dist = self.dfs(visited, graph, nei)
                if dist > max1:
                    max2 = max1
                    max1 = dist
                elif dist > max2:
                    max2 = dist
        visited.remove(node)
        self.res = max(self.res, max1 + max2)
        return max1 + 1