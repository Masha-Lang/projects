#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream in;
    ofstream out;
    string x;
    in.open("in.txt");
    out.open("out.txt");
    while (getline(in, x)) {
        cout<<x<<endl;
    }
    out<<"OUT";
    cout<<"Hello World!"<<endl;
    in.close();
    out.close();
    return 0;
}   