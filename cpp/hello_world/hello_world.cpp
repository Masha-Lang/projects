#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream input("input.txt");
    ofstream output("output.txt");
    int max, x;
    string line, k;
    input >> max;
    while (getline(input, line)) {
        k += line;
    }
    line = k;
    //while(k.size()>0) {
    cout << line << k << endl;
    line.resize(max);
    cout << line << endl;
        //for(int i=max-1; i>0; i--) {
            
        //}
    //}
    
    input.close();
    output.close();
    return 0;
}