#include <bits/stdc++.h>
#include <stdio.h> 
using namespace std; 

int main() {
    char s[30];
    cin >> s; 

    for (size_t i = 0; i < strlen(s); ++i) {
        if (s[i] == 'a')
            s[i] = 'a' + 1; 
    }
    cout << s << endl; 
}