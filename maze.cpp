#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <tuple>

using namespace std;

char maze[500][500];
int n, m, k;

void printMaze() {
    for(int i=0; i < n; i++) {
        for(int j=0; j < m; j++) {
            char c;
            if(maze[i][j] == 1)
                c = '#';
            else if(maze[i][j] == 0 || maze[i][j] == 3)
                c = '.';
            else
                c = 'X';
            cout << c;
        }
        cout << endl;
    }
}

int markArea(int i, int j, int replaceable) {
    int replaced = 0;
    if(maze[i][j] == 0) {
        maze[i][j] = 3;
        if(j > 0)
            replaced += markArea(i, j-1, replaceable - replaced);
        if(j < m-1)
            replaced += markArea(i, j+1, replaceable - replaced);
        if(i > 0)
            replaced += markArea(i-1, j, replaceable - replaced);
        if(i < n-1)
            replaced += markArea(i+1, j, replaceable - replaced);

        if(replaceable - replaced > 0) {
            maze[i][j] = 2;
            replaced ++;
        }
    }
    return replaced;
}

int main(void)
{
    cin >> n >> m >> k; // n=height, m=width, k=nbWalls

    for(int i=0; i < n; i++) {
        for(int j=0; j < m; j++) {
            char c;
            cin >> c;
            if(c == '#')
                maze[i][j] = 1;
            else
                maze[i][j] = 0;
        }
    }

    for(int i=0; i < n; i++) {
        for(int j=0; j < m; j++) {
            if(maze[i][j] == 0) {
                markArea(i, j, k);
                break;
            }
        }
    }

    printMaze();

    return 0;
}
