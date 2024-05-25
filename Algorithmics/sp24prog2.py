import heapq
import sys

def read_graph(filename):
    with open(filename, 'r') as file:
        vertices, edges = map(int, file.readline().strip().split())
        graph = []
        for line in file:
            u, v, w = map(int, line.strip().split())
            graph.append((u, v, w))
    return vertices, graph

def detect_negative_cycle(vertices, graph):
    distance = [float('inf')] * vertices
    distance[0] = 0

    for _ in range(vertices - 1):
        for u, v, w in graph:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in graph:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            return True, distance
    return False, distance

def bellman_ford(vertices, graph):
    distance = [float('inf')] * vertices
    distance[0] = 0

    for _ in range(vertices - 1):
        for u, v, w in graph:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    return distance

def dijkstra(vertices, graph):
    distance = [float('inf')] * vertices
    distance[0] = 0
    pq = [(0, 0)]  # (distance, vertex)
    adj = {i: [] for i in range(vertices)}
    for u, v, w in graph:
        adj[u].append((v, w))

    while pq:
        dist, u = heapq.heappop(pq)
        if dist > distance[u]:
            continue
        for v, weight in adj[u]:
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                heapq.heappush(pq, (distance[v], v))
    return distance

def dag_shortest_path(vertices, graph):
    def topological_sort(vertices, adj):
        indegree = [0] * vertices
        for u in adj:
            for v, _ in adj[u]:
                indegree[v] += 1

        stack = [i for i in range(vertices) if indegree[i] == 0]
        topo_order = []

        while stack:
            u = stack.pop()
            topo_order.append(u)
            for v, _ in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    stack.append(v)
        return topo_order

    distance = [float('inf')] * vertices
    distance[0] = 0
    adj = {i: [] for i in range(vertices)}
    for u, v, w in graph:
        adj[u].append((v, w))

    topo_order = topological_sort(vertices, adj)
    for u in topo_order:
        if distance[u] != float('inf'):
            for v, weight in adj[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
    return distance

def main():
    vertices, graph = read_graph('input.txt')
    has_negative_cycle, distance = detect_negative_cycle(vertices, graph)

    if has_negative_cycle:
        print("No shortest paths can be found.")
    else:
        if any(w < 0 for _, _, w in graph):
            distance = bellman_ford(vertices, graph)
        elif any(v > u for u, v, _ in graph):
            distance = dag_shortest_path(vertices, graph)
        else:
            distance = dijkstra(vertices, graph)

        print("Shortest paths from vertex 0:")
        for i in range(vertices):
            print(f"Vertex {i}: {distance[i]}")

if __name__ == "__main__":
    main()
