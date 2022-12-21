#include <stdio.h>

struct edge {
    int u, v, w;
};

struct graph {
    int V, E;
    struct edge* edges;
};

struct graph* make_graph () {
    struct graph* new_graph;
    new_graph->E = 0;
    new_graph->V = 0;
    new_graph->edges = (struct edge *)malloc(sizeof(struct edge));
}



void insert_edge (struct graph* graph, u,v ) {

}


int main () {

    return 0;
}