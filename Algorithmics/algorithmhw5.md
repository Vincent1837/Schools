---
marp: true
theme: default
math: mathjax
size: 4:3

---

# Algorithm Homework 5

---


### 22.1-3

We can modify the *Bellman-Ford* algorithm to keep track of **whether any distance estimates change** during each pass over the edges. If an entire pass occurs without any distance estimate changes, terminate the algorithm early. 

This ensures the algorithm will terminate in at most $m+1$ passes.

---

```javascript
BellmanFord(G, w, s):
   for each vertex v in G:
      v.d = ∞
      v.π = NIL
   s.d = 0
   for i = 1 to |V| - 1:
      changed = false
      for each edge (u, v) in E:
         if u.d + w(u, v) < v.d:
            v.d = u.d + w(u, v)
            v.π = u
            changed = true
      if not changed:
         break
   for each edge (u, v) in E:
      if u.d + w(u, v) < v.d:
         return "Graph contains a negative-weight cycle"
   return (d, π)
```

---

### 22.1-5

The *Bellman-Ford* algorithm inherently runs in $O(VE)$ time because it relaxes all edges $V - 1$ times. Since each edge relaxation takes constant time and there are $E$ edges, each pass over all edges takes $O(E)$ time, resulting in $O(VE)$ for $V - 1$ passes.

To modify the *Bellman-Ford* algorithm for adjacency lists, iterate over all vertices and relax all outgoing edges from each vertex. This ensures that each edge is considered once per pass, maintaining the $O(VE)$ time complexity.

---


```javascript
BellmanFordAdjList(G, w, s):
   for each vertex v in G:
      v.d = ∞
      v.π = NIL
   s.d = 0
   for i = 1 to |V| - 1:
      for each vertex u in V:
         for each vertex v in Adj[u]:
            if u.d + w(u, v) < v.d:
               v.d = u.d + w(u, v)
               v.π = u
   for each vertex u in V:
      for each vertex v in Adj[u]:
         if u.d + w(u, v) < v.d:
            return "Graph contains a negative-weight cycle"
   return (d, π)
```

---

### 22.1-6

1. Initialize $\delta^*(v) = \infty$ for all $v \in V$.
2. For each vertex $u \in V$:
   - Run *Bellman-Ford* with $u$ as the source.
   - For each vertex $v \in V$, update $\delta^*(v)$ to be the minimum of its current value and the distance from $u$ to $v$.

Since *Bellman-Ford* runs in $O(VE)$ and is executed $V$ times, the total time complexity is $O(V^2E)$.

---

```javascript
FindMinDistances(G, w):
   for each vertex v in G:
      δ*(v) = ∞
   for each vertex u in G:
      (d, π) = BellmanFord(G, w, u)
      for each vertex v in G:
         if d[v] < δ*(v):
            δ*(v) = d[v]
   return δ*

BellmanFord(G, w, s):
   for each vertex v in G:
      v.d = ∞
      v.π = NIL
   s.d = 0
   for i = 1 to |V| - 1:
      for each edge (u, v) in E:
         if u.d + w(u, v) < v.d:
            v.d = u.d + w(u, v)
            v.π = u
   for each edge (u, v) in E:
      if u.d + w(u, v) < v.d:
         return "Graph contains a negative-weight cycle"
   return (d, π)
```

---

### 22.2-2

The change ensures that each vertex is processed only once in topological order, which maintains the correctness of the algorithm.  

The topological sort guarantees that by the time a vertex $u$ is processed, all vertices $v$ with edges $(v, u)$ have already been processed.

This preserves the invariant that each vertex $u$ has the correct shortest path distance when it is processed.

---

### 22.3-3

**The proposed algorithm is not correct.**

Dijkstra's algorithm must process all vertices to ensure that all shortest path estimates are finalized. Terminating the loop early means the shortest path to the last vertex in the priority queue $Q$ might not be correctly computed.

---

### 22.3-5

1. Initialize an empty set of edges $S$.
2. For each vertex $v \in V$:
   - If $v \neq s$, add the edge $(\pi(v), v)$ to $S$.
3. Check that $S$ forms a spanning tree:
   - Ensure $|S| = |V| - 1$.
   - Use a union-find data structure to check that $S$ forms a single connected component without cycles.
4. Verify the shortest path properties:
   - For each edge $(u, v) \in E$, check that $v.d \leq u.d + w(u, v)$. If any check fails, return "Incorrect".
   - For each edge $(u, v) \in S$, ensure $v.d = u.d + w(u, v)$

---

If all checks pass, the attributes are correct. This verification runs in $O(V + E)$ time.

```javascript
CheckDijkstraOutput(G, w, s, d, π):
   // Step 1: Initialize an empty set of edges S
   S = ∅

   // Step 2: Build the set of edges S from π values
   for each vertex v in G:
      if v ≠ s:
         if π[v] ≠ NIL:
            S = S ∪ {(π[v], v)}

   // Step 3: Check that S forms a spanning tree
   if |S| ≠ |V| - 1:
      return "Incorrect"
   if not isSingleConnectedComponent(S, G):
      return "Incorrect"

    // Step 4: Verify shortest path properties
   for each edge (u, v) in E:
      if d[v] > d[u] + w(u, v):
         return "Incorrect"
   for each edge (u, v) in S:
      if d[v] ≠ d[u] + w(u, v):
         return "Incorrect"

   return "Correct"

```

---

```javascript
isSingleConnectedComponent(S, G):
   // Use union-find to check if S forms a single connected component
   uf = UnionFind(|V|)
   for each edge (u, v) in S:
      uf.union(u, v)
   root = uf.find(0)
   for each vertex v in G:
      if uf.find(v) ≠ root:
         return false
   return true
```

---

### 22.4-3

**No, the shortest-path weight from the new vertex $v_0$ in a constraint graph cannot be positive.**

The purpose of adding $v_0$ with edges to all other vertices with weight zero is to initialize the *Bellman-Ford* algorithm, ensuring that the shortest-path weights are calculated correctly. 

Since the edge weights from $v_0$ are zero, the shortest-path weights from $v_0$ to any vertex will not be positive.

---

### 22.4-8

Let $Ax \leq b$ be a system of $m$ difference constraints in $n$ unknowns. Construct the corresponding constraint graph, where each constraint $x_i - x_j \leq b_k$ is represented as an edge $(j, i)$ with weight $b_k$.

Running the *Bellman-Ford* algorithm on this graph will maximize $\sum_{i=1}^n x_i$ subject to $Ax \leq b$ and $x_i \leq 0$ for all $x_i$. This is because *Bellman-Ford* finds the shortest paths, effectively distributing the largest possible values to $x_i$ while respecting the constraints.

---

### 22.4-9

The *Bellman-Ford* algorithm, when run on the constraint graph for a system $Ax \leq b$ of difference constraints, minimizes the quantity $(\max \{ x_i \} - \min \{ x_i \})$ subject to $Ax \leq b$. 

This fact is useful in scheduling construction jobs because it ensures the smallest possible range of start times, leading to a more compact schedule and potentially reducing the overall project duration.

---

### 22.5-2

Consider the graph $G$ with vertices $\{s, u, v\}$ and edges $\{(s, u), (s, v), (u, v)\}$ with weights $w(s, u) = 1$, $w(s, v) = 2$, and $w(u, v) = 1$. 

The shortest-path tree rooted at $s$ containing the edge $(u, v)$ is $\{(s, u), (u, v)\}$. 

Another shortest-path tree rooted at $s$ that does not contain the edge $(u, v)$ is $\{(s, u), (s, v)\}$.

---

### 22.5-5

Consider the graph $G$ with vertices $\{s, u, v\}$ and edges $\{(s, u), (u, v), (v, s)\}$ with weights $w(s, u) = 1$, $w(u, v) = 1$, and $w(v, s) = 1$. 

Assign $\pi(u) = s$, $\pi(v) = u$, and $\pi(s) = v$. This assignment of $\pi$ values creates a cycle $G_\pi$ because it implies a predecessor chain $s \to u \to v \to s$. 

According to Lemma 22.16, such an assignment cannot be produced by a sequence of relaxation steps, confirming the presence of a cycle.

---

### 22-2 Nesting Boxes

#### a. Argue that the nesting relation is transitive.

To show that the nesting relation is transitive, assume we have three boxes $A$, $B$, and $C$ such that $A$ nests within $B$ and $B$ nests within $C$.

Let the dimensions of the boxes be:
- $A: (a_1, a_2, \ldots, a_d)$
- $B: (b_1, b_2, \ldots, b_d)$
- $C: (c_1, c_2, \ldots, c_d)$

---


Since $A$ nests within $B$, there exists a permutation $\pi$ such that:
$a_{\pi(1)} < b_1, a_{\pi(2)} < b_2, \ldots, a_{\pi(d)} < b_d$

Similarly, since $B$ nests within $C$, there exists a permutation $\sigma$ such that:
$b_{\sigma(1)} < c_1, b_{\sigma(2)} < c_2, \ldots, b_{\sigma(d)} < c_d$

To prove transitivity, we need to show that there exists a permutation $\tau$ such that:
$a_{\tau(1)} < c_1, a_{\tau(2)} < c_2, \ldots, a_{\tau(d)} < c_d$

---

Construct $\tau$ by following $\pi$ and $\sigma$. For each $i$, set $\tau(i) = \pi(\sigma(i))$. 

This ensures that:
$a_{\tau(1)} = a_{\pi(\sigma(1))} < b_{\sigma(1)} < c_1$
$a_{\tau(2)} = a_{\pi(\sigma(2))} < b_{\sigma(2)} < c_2$
$\vdots$
$a_{\tau(d)} = a_{\pi(\sigma(d))} < b_{\sigma(d)} < c_d$

Thus, $A$ nests within $C$, proving that the nesting relation is transitive.

---

#### b. Describe an efficient method to determine whether one $d$-dimensional box nests inside another.

1. Sort the dimensions of both boxes $A$ and $B$ in non-decreasing order.
2. Compare the sorted dimensions element-wise. If for all $i$, the $i$-th dimension of $A$ is less than the $i$-th dimension of $B$, then $A$ nests within $B$.

```javascript
canNest(A, B):
   sort(A)
   sort(B)
   for i from 1 to d:
      if A[i] >= B[i]:
         return False
   return True
```

This method runs in $O(d \ln d)$ time due to the sorting step.

---

#### c. Find the longest sequence of $d$-dimensional boxes that nest within each other.

1. Sort each box's dimensions.
2. Sort the list of boxes based on the first dimension, then the second dimension, and so on.
3. Use dynamic programming to find the longest increasing subsequence (LIS) where each box can nest inside the next one.

###### Running Time:

- Sorting the dimensions of each box: $O(nd \ln d)$
- Sorting the list of boxes lexicographically: $O(nd \ln n)$
- Finding the LIS: $O(n^2d)$

---

```javascript
longestNestingSequence(boxes):
   for each box in boxes:
      sort(box)
   sort(boxes, lexicographically)
    
   // LIS based on dimensions comparison
   n = length(boxes)
   dp = array of size n, all initialized to 1
   for i from 1 to n-1:
      for j from 0 to i-1:
         if canNest(boxes[j], boxes[i]):
            dp[i] = max(dp[i], dp[j] + 1)
    
   return max(dp)

canNest(A, B):
   for i from 1 to d:
      if A[i] >= B[i]:
         return False
   return True
```

---

### 22-3 Arbitrage

#### a. Algorithm to Determine Arbitrage Opportunity

we can use a graph-based approach with the *Bellman-Ford* algorithm. The key idea is to take the logarithm of the exchange rates to transform the problem into finding a negative-weight cycle in the graph.

1. **Transform the Exchange Rates:**
   Convert each exchange rate $R[i, j]$ to a weight by taking the negative logarithm: $w[i, j] = -\log(R[i, j])$

2. **Detect Negative-Weight Cycle:**
   Use the *Bellman-Ford* algorithm to find a negative-weight cycle in the graph. If such a cycle exists, it corresponds to an arbitrage opportunity.

---

It runs in $O(n^3)$ for a graph with $n$ vertices and $n^2$ edges.


```javascript
detectArbitrage(R):
   n = length(R)
   // Step 1: Transform exchange rates
   for i from 1 to n:
      for j from 1 to n:
         w[i][j] = -log(R[i][j])

   // Step 2: Use Bellman-Ford to detect negative cycle
   // Initialize distances
   dist = array of size n, all initialized to infinity
   dist[1] = 0 // Start from any vertex, here 1
    
   // Relax edges up to n-1 times
   for k from 1 to n-1:
      for i from 1 to n:
         for j from 1 to n:
            if dist[i] + w[i][j] < dist[j]:
               dist[j] = dist[i] + w[i][j]
    
   // Check for negative-weight cycle
   for i from 1 to n:
      for j from 1 to n:
         if dist[i] + w[i][j] < dist[j]:
            return True // Negative cycle detected

   return False // No negative cycle
```

---

#### b. Algorithm to Print Arbitrage Sequence

```javascript
findArbitrageSequence(R):
   n = length(R)
   // Step 1: Transform exchange rates
   for i from 1 to n:
      for j from 1 to n:
         w[i][j] = -log(R[i][j])

   // Step 2: Use Bellman-Ford to detect negative cycle
   // Initialize distances and predecessors
   dist = array of size n, all initialized to infinity
   pred = array of size n, all initialized to NIL
   dist[1] = 0 // Start from any vertex, here 1
    
   // Relax edges up to n-1 times
   for k from 1 to n-1:
      for i from 1 to n:
         for j from 1 to n:
            if dist[i] + w[i][j] < dist[j]:
               dist[j] = dist[i] + w[i][j]
               pred[j] = i
    
   // Check for negative-weight cycle and find the cycle
   for i from 1 to n:
      for j from 1 to n:
         if dist[i] + w[i][j] < dist[j]:
            // Negative cycle detected, reconstruct the cycle
            cycle = []
            visited = array of size n, all initialized to False
            x = i
            // Follow predecessors to find the cycle
            while not visited[x]:
               visited[x] = True
               x = pred[x]
            start = x
            cycle.append(start)
            x = pred[start]
            while x != start:
               cycle.append(x)
               x = pred[x]
            cycle.append(start)
            cycle.reverse()
            return cycle

   return None // No negative cycle
```

---

### 23.1-2