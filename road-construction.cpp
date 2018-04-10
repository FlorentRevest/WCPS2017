#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

using namespace std;

int main(void)
{
    int n, m;
    cin >> n >> m;
    bool possible[1000];

    for(int i=0; i < n; i++)
        possible[i] = true;

    for(int i=0; i < m; i++) {
        int src = 0;
        int dest = 0;
        cin >> src >> dest;
        src --;
        dest --;
        possible[src] = false;
        possible[dest] = false;
    }

    int centerOfKingdom=0;
    while(centerOfKingdom < n && !possible[centerOfKingdom])
        centerOfKingdom++;

    cout << n-1 << endl;

    for(int i=0; i < n; i++)
        if(i != centerOfKingdom)
            cout << i+1 << " " << centerOfKingdom+1 << endl;

    return 0;
}
