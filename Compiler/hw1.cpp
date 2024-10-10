#include <iostream>
#include <string>

using namespace std;


int main () {
    string input;
    while (getline(cin, input)) {
        cout << "hello, " << input << endl;
    }
    return 0;
}