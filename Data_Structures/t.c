#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_VERTICES 1000
#define INF 2147483647

int V, E;
int adj[MAX_VERTICES][MAX_VERTICES];

int minKey(int key[], int mstSet[])
{
   int min = INF, min_index;
 
   for (int v = 0; v < V; v++)
     if (mstSet[v] == 0 && key[v] < min)
         min = key[v], min_index = v;
 
   return min_index;
}
 
int printMST(int parent[], int n, int graph[V][V])
{
   printf("Edge   Weight\n");
   int cost = 0;
   for (int i = 1; i < V; i++)
   {
      printf("%d - %d    %d \n", parent[i], i, graph[i][parent[i]]);
      cost += graph[i][parent[i]];
   }
   return cost;
}
 
void primMST(int graph[V][V])
{
     int parent[V];
     int key[V];
     int mstSet[V];
 
     for (int i = 0; i < V; i++)
        key[i] = INF, mstSet[i] = 0;
 
     key[0] = 0;
     parent[0] = -1;
 
     for (int count = 0; count < V-1; count++)
     {
        int u = minKey(key, mstSet);
 
        mstSet[u] = 1;
 
        for (int v = 0; v < V; v++)
 
           if (graph[u][v] && mstSet[v] == 0 && graph[u][v] <  key[v])
             parent[v]  = u, key[v] = graph[u][v];
     }
 
     printf("Minimum spanning tree cost: %d\n", printMST(parent, V, graph));
}



int main() {
    // read matrix info 
    scanf("%d", &V);
    int matrix[V][V];
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }


    primMST(matrix);


    return 0;
}
