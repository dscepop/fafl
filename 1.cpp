#include <iostream> 
#include <string> 
using namespace std; 
 
enum State { 
    S0, S1, S2, S3 
}; 
 
bool acceptsString(const string& input) { 
    State currentState = S0; 
 
    for (char c : input) { 
        switch (currentState) { 
            case S0: 
                if (c == '1') { 
                    currentState = S1; 
                } // else stay in S0 (on '0') 
                break; 
            case S1: 
                if (c == '1') { 
                    currentState = S2; 
                } else { 
                    currentState = S0; // on '0', go back to S0 
                } 
                break; 
            case S2: 
                if (c == '1') { 
                    currentState = S3; 
                } else { 
                    currentState = S0; // on '0', go back to S0 
                } 
                break; 
            case S3: 
                // Once we reach S3, we stay in S3 (accepting state) 
                break; 
        } 
    } 
    return currentState == S3; 
} 
 
int main() { 
    string input; 
    cout << "Enter a binary string: "; 
    cin >> input; 
 
    if (acceptsString(input)) { 
        cout << "Accepted (contains 111)" << endl; 
    } else { 
cout << "Rejected (does not contain 111)" << endl; 
} 
return 0; 
}