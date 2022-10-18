/*
* Practice 8
* Name: 蔡淵丞
* Student Number: 11052567
* Course: 2021-CE1003-B
*/
#include <iostream>
using namespace std;

int main()
{
    string N, I;
    double E, M, C;
    int WE, WM, WC;

    cout << "Please input your name : "; cin >> N;
    
    cout << "please input your student ID : "; cin >> I;
    
    cout << "English score : "; cin >> E;

    cout <<"Math score : "; cin >> M;
    
    cout << "Chinese score : "; cin >> C;
    
    cout << "English weight : "; cin >> WE;
    
    cout << "Math weight : "; cin >> WM;
    
    cout << "Chinese weight : "; cin >> WC;
    
    int AA = (E + M + C) / 3;
    int WA = (E*WE + M*WM + C*WC) / (WE+WM+WC);

    cout << "\nStudent name : " << N << endl;
    cout << "Student ID : " << I << endl;
    cout << "Aritmetic average : " << AA << endl;
    cout << "Weighted average : " << WA << endl;

    return 0;
}