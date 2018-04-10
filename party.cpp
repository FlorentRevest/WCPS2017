#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

using namespace std;

int layersNb(int i, vector<int> *pi) {
    int manager = pi->at(i);
    if(manager != -2)
        return 1 + layersNb(manager, pi);
    else
        return 1;
}

int main(void)
{
    int n;
    vector<int> pi;
    cin >> n;
    for(int i=0; i < n; i++) {
        int v;
        cin >> v;
        pi.push_back(v-1);
    }

    int maxLayers = 0;
    for(int i=0; i < n; i++) {
        int curLayersNb = layersNb(i, &pi);
        if(curLayersNb > maxLayers)
            maxLayers = curLayersNb;
    }

    cout << maxLayers << endl;

    return 0;
}
