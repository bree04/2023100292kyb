from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]
        for neighbor in sorted(self.adj_list[start]): 
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        return result

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for neighbor in sorted(self.adj_list[vertex]): 
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def find_connected_components(self):
        visited = set()
        components = []

        for vertex in sorted(self.adj_list.keys()):  
            if vertex not in visited:
                component = self.bfs(vertex)
                components.append(component)
                visited.update(component)
        return components

    def spanning_tree(self, start):
        visited = set()
        edges = []
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            for neighbor in sorted(self.adj_list[vertex]):  
                if neighbor not in visited:
                    visited.add(neighbor)
                    edges.append((vertex, neighbor))
                    queue.append(neighbor)
        return edges



print("Vertex를 입력하세요 (예: A B C D E F G H):")
vertices = input().split()
print("Edge를 입력하세요 (예: A-B A-C B-D ...):")
edges = input().split()

graph = Graph()
for edge in edges:
    u, v = edge.split('-')
    graph.add_edge(u, v)

print("\nDFS:", " - ".join(graph.dfs(vertices[0])))
print("BFS:", " - ".join(graph.bfs(vertices[0])))

components = graph.find_connected_components()
print("\nConnected Components:")
for i, component in enumerate(components):
    print(f"Component {i + 1}:", " - ".join(component))

spanning_tree_edges = graph.spanning_tree(vertices[0])
print("\nSpanning Tree Edges:")
for edge in spanning_tree_edges:
    print(f"{edge[0]}-{edge[1]}")
