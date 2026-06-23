class Solution(object):
    def validPath(self, n, edges, source, destination):
        if source==destination:
            return True
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue=deque([source])
        visited=set([source])
        while queue:
            current=queue.popleft()
            if current==destination:
                return True
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False