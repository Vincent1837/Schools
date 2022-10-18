/*
* Assignment 9
* Name: 蔡淵丞
* Student Number: 11052567
* Course: 2021-CE1003-B
*/
# include <bits/stdc++.h>
using namespace std;

int main (){
    int a, b, c, maximum, mid, minimum;
    cout << "Enter a: "; cin >> a;
    cout << "Enter b: "; cin >> b;
    cout << "Enter c: "; cin >> c;

    int arr[3] = {a, b, c};
    sort(arr, arr+3);

    if (arr[2] >= arr[1] + arr[0]){
        cout << "Not triangle" << "\n";
    }
    else if (arr[2]*arr[2] == arr[1]*arr[1] + arr[0]*arr[0]){
        cout << "Right triangle\n";
    }
    else if (arr[0] == arr[1] and arr[1] == arr[2]){
        cout << "Regular triangle\n";
    }
    else if (arr[0] == arr[1]){
        cout << "Isosceles triangle\n";
    }
    else {
        cout << "Triangle\n";
    }

    return 0;
}