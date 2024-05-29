import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []
        self.adj_list = {i: [] for i in range(vertices)}
        self.has_neg_weight_edges = False
        self.has_neg_weight_cycles = False

    def add_edge(self, u, v, w):
        if w < 0:
            self.has_neg_weight_edges = True
        self.edges.append((u, v, w))
        self.adj_list[u].append((v, w))

    def bellman_ford(self, source):
        dist = [float("Inf")] * self.V
        dist[source] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.edges:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                self.has_neg_weight_cycles = True
                return dist, True

        return dist, False

    def dijkstra(self, source):
        dist = [float('Inf')] * self.V
        dist[source] = 0
        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, u = heapq.heappop(priority_queue)

            if current_distance > dist[u]:
                continue

            for neighbor, weight in self.adj_list[u]:
                distance = current_distance + weight

                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return dist

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

    def detect_negative_cycles(self):
        for vertex in range(self.V):
            dist, has_cycle = self.bellman_ford(vertex)
            if has_cycle:
                self.has_neg_weight_cycles = True
                return

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for edge in self.adj_list[v]:
            if not visited[edge[0]]:
                self.topological_sort_util(edge[0], visited, stack)
        stack.insert(0, v)

    def is_dag_util(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        for u, v, _ in self.edges:
            if stack.index(u) > stack.index(v):
                return False
        return True

    def dag_shortest_path(self, source):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        
        dist = [float("Inf")] * self.V
        dist[source] = 0

        while stack:
            u = stack.pop(0)
            for edge in self.edges:
                if edge[0] == u:
                    v = edge[1]
                    weight = edge[2]
                    if dist[u] != float("Inf") and dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight

        return dist

    def classify_graph(self):
        self.detect_negative_cycles()
        if self.has_neg_weight_cycles:
            return "A"
        elif self.has_neg_weight_edges:
            return "B"
        elif not self.has_neg_weight_edges:
            if self.is_dag_util():
                return "D"
            else:
                return "C"

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        vertices, edges = map(int, file.readline().split())
        graph = Graph(vertices)
        for line in file:
            u, v, w = map(int, line.split())
            graph.add_edge(u, v, w)

    graph_type = graph.classify_graph()
    print(f"Graph type: {graph_type}")

    if graph_type == "A":
        dist, has_cycle = graph.bellman_ford(0)
        if has_cycle:
            print("No shortest paths can be found.")
        else:
            print("Using Bellmanford")
            graph.print_solution(dist)
    elif graph_type == "D":
        print("Using DAG shortest paths")
        dist = graph.dag_shortest_path(0)
        graph.print_solution(dist)
    elif graph_type == "C":
        print("Using Dijkstra's")
        dist = graph.dijkstra(0)
        graph.print_solution(dist)
    else:
        print("Using Bellmanford")
        dist, _ = graph.bellman_ford(0)
        graph.print_solution(dist)

if __name__ == "__main__":
    main()