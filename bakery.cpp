#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <climits>

using namespace std;

struct vertex;

struct link {
    int cost;
    int end;
};

struct vertex {
    bool hasFlour;
    vector<link> adj;
};

int main(void)
{
    int minRubles = INT_MAX;
    int n, m, k;
    cin >> n >> m >> k;
    vector<struct vertex> vertices;
    vertices.reserve(n);

    for(int i=0; i < n; i++) {
        struct vertex vert;
        vert.hasFlour = false;
        vertices.push_back(vert);
    }

    for(int i=0; i < m; i++) {
        int u, v, l;
        cin >> u >> v >> l;
        vertices[u-1].adj.push_back({.cost = l, .end = v-1});
        vertices[v-1].adj.push_back({.cost = l, .end = u-1});
    }

    for(int i=0; i < k; i++) {
        int nb;
        cin >> nb;
        vertices[nb-1].hasFlour = true;
    }

    for(struct vertex vert : vertices)
        if(vert.hasFlour)
            for(struct link l : vert.adj)
                if(!vertices[l.end].hasFlour)
                    if(l.cost < minRubles)
                        minRubles = l.cost;

    if(minRubles != INT_MAX)
        cout << minRubles << endl;
    else
        cout << "-1" << endl;
    return 0;
}
