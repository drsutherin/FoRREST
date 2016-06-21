
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
    string pass = "";
    
    cout << "Please enter password: ";
    cin >> pass;
    
    if (!pass.compare("coolpass"))
        cout << "You're correct!" << endl;
    else
        cout << "You're wrong!" << endl;
    
    return 0;
}
