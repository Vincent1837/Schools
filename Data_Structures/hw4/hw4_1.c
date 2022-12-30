#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_EDGES 100000
#define MAX_VERTICES 1000
#define INF 2147483647

typedef struct
{
    int u, v, w;
} Edge;

int V, E;
Edge edges[MAX_EDGES];

int parent[MAX_VERTICES];


int find(int u)
{
    if (parent[u] != u)
        parent[u] = find(parent[u]);
    return parent[u];
}

void unionn(int u, int v)
{
    int p1 = find(u);
    int p2 = find(v);
    parent[p1] = p2;
}

void kruskal () {
    // sort the edges by weight
    for (int i = 0; i < E; i++) {
        for (int j = 0; j < E - 1; j++) {
            if (edges[j].w > edges[j+1].w) {
                Edge temp = edges[j];
                edges[j] = edges[j+1];
                edges[j+1] = temp;
            }
        }
    }

    for (int i = 1; i <= V; i++)
        parent[i] = i;

    int count = 0, cost = 0;
    for (int i = 0; count < V - 1; i++)
    {
        int u = edges[i].u;
        int v = edges[i].v;
        int w = edges[i].w;
        if (find(u) != find(v))
        {
            unionn(u, v);
            count++;
            cost += w;
        }
    }
    printf("Kruskal minimum cost: %d\n", cost);
}

int minKey(int key[], int mstSet[])
{
   int min = INF, min_index;
 
   for (int v = 0; v < V; v++)
     if (mstSet[v] == 0 && key[v] < min)
         min = key[v], min_index = v;
 
   return min_index;
}
 
int primMST_cost(int parent[], int n, int graph[V][V]){
   int cost = 0;
   for (int i = 1; i < V; i++){
      cost += graph[i][parent[i]];
   }
   return cost;
}
 
void primMST(int graph[V][V]) {
    int parent[V];
    int key[V];
    int mstSet[V];

    for (int i = 0; i < V; i++){
        key[i] = INF, mstSet[i] = 0;
    }

    key[0] = 0;
    parent[0] = -1;

    for (int count = 0; count < V-1; count++){
        int u = minKey(key, mstSet);

        mstSet[u] = 1;

        for (int v = 0; v < V; v++){
            if (graph[u][v] && mstSet[v] == 0 && graph[u][v] <  key[v]){
                parent[v]  = u, key[v] = graph[u][v];
            }
        }

    }
    int cost = 0;
    for (int i = 1; i < V; i++){
        cost += graph[i][parent[i]];
    }
    printf("Prim minimum cost: %d\n", cost);
}

int main() {
    while (1) {
        // read matrix info 
        scanf("%d", &V);
        if (V == -1) {
            return 0;
        }
        int matrix[V][V];
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                scanf("%d", &matrix[i][j]);
            }
        }

        // construct the graph from matrix
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (j > i && matrix[i][j]) {
                    Edge new_edge;
                    new_edge.u = i;
                    new_edge.v = j;
                    new_edge.w = matrix[i][j];
                    edges[E++] = new_edge;
                }
            }
        }

        kruskal();
        primMST(matrix);

    }

    return 0;
}
