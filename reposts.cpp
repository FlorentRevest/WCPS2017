#include <iostream>
#include <sstream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <string>

using namespace std;

struct repost{
    string reposter;
    int indexReposted;
};

int indexOf(string reposted, vector<struct repost> *pi) {
    if(reposted == "POLYCARP")
        return -1;
    else {
        int i = 0;
        for(struct repost rt : *pi) {
            if(rt.reposter == reposted)
                return i;
            i ++;
        }
        return -1;
    }
}

int layersNb(int i, vector<struct repost> *pi) {
    struct repost rt = pi->at(i);
    if(rt.indexReposted != -1)
        return 1 + layersNb(rt.indexReposted, pi);
    else
        return 1;
}

int main(void)
{
    int n;
    cin >> n;
    string ign;
    getline(cin, ign);
    vector<struct repost> pi;
    for(int i=0; i < n; i++) {
        string line;
        getline(cin, line);

        stringstream ss(line);
        string ignored, reposted;

        struct repost rt;
        ss >> rt.reposter;
        for (auto & c: rt.reposter) c = toupper(c);

        ss >> ignored;
        ss >> reposted;
        for (auto & c: reposted) c = toupper(c);
    
        rt.indexReposted = indexOf(reposted, &pi);

        pi.push_back(rt);
    }

    int maxLayers = 0;
    for(int i=0; i < n; i++) {
        int curLayersNb = layersNb(i, &pi);
        if(curLayersNb > maxLayers)
            maxLayers = curLayersNb;
    }

    cout << maxLayers+1 << endl;

    return 0;
}
