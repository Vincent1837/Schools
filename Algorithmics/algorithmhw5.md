---
marp: true
theme: uncover 
math: mathjax
---

# Algorithm Homework 5

---

### 22.1-3

Modify the *Bellman-Ford* algorithm to keep track of **whether any distance estimates change** during each pass over the edges. If an entire pass occurs without any distance estimate changes, terminate the algorithm early. This ensures the algorithm will terminate in at most $m+1$ passes.

---

### 22.1-5

The *Bellman-Ford* algorithm inherently runs in $O(VE)$ time because it relaxes all edges $V - 1$ times. Since each edge relaxation takes constant time and there are $E$ edges, each pass over all edges takes $O(E)$ time, resulting in $O(VE)$ for $V - 1$ passes.

To modify the *Bellman-Ford* algorithm for adjacency lists, iterate over all vertices and relax all outgoing edges from each vertex. This ensures that each edge is considered once per pass, maintaining the $O(VE)$ time complexity.

---

### 22.1-6

1. Initialize $\delta^*(v) = \infty$ for all $v \in V$.
2. For each vertex $u \in V$:
   - Run Bellman-Ford with $u$ as the source.
   - For each vertex $v \in V$, update $\delta^*(v)$ to be the minimum of its current value and the distance from $u$ to $v$.

Since *Bellman-Ford* runs in $O(VE)$ and is executed $V$ times, the total time complexity is $O(V^2E)$.

---

### 22.2-2

The change ensures that each vertex is processed only once in topological order, which maintains the correctness of the algorithm. The topological sort guarantees that by the time a vertex $u$ is processed, all vertices $v$ with edges $(v, u)$ have already been processed. This preserves the invariant that each vertex $u$ has the correct shortest path distance when it is processed.

---

### 22.3-3

The proposed algorithm is not correct. Dijkstra's algorithm must process all vertices to ensure that all shortest path estimates are finalized. Terminating the loop early means the shortest path to the last vertex in the priority queue $Q$ might not be correctly computed.

---

### 22.3-5

1. Initialize an empty set of edges $S$.
2. For each vertex $v \in V$:
   - If $v \neq s$, add the edge $(\pi(v), v)$ to $S$.
3. Check that $S$ forms a spanning tree:
   - Ensure $|S| = |V| - 1$.
   - Use a union-find data structure to check that $S$ forms a single connected component without cycles.

---

4. Verify the shortest path properties:
   - For each edge $(u, v) \in E$, check that $v.d \leq u.d + w(u, v)$. If any check fails, return "Incorrect".
   - For each edge $(u, v) \in S$, ensure $v.d = u.d + w(u, v)$.

If all checks pass, the attributes are correct. This verification runs in $O(V + E)$ time.
