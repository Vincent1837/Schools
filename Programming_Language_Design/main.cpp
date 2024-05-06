#include <iostream>
#include <vector>
using namespace std;

// Implement class FunctionalList
template <typename T>
class FunctionalList {
private:
    vector<T> list;

public:
    void add(T element) {
        list.push_back(element);
    }

    T head() {
        return list[0];
    }

    T last() {
        return list[list.size() - 1];
    }

    vector<T> tail() {
        vector<T> newList;
        for (int i = 1; i < list.size(); i++) {
            newList.push_back(list[i]);
        }
        return newList;
    }

    vector<T> init() {
        vector<T> newList;
        for (int i = 1; i < list.size(); i++) {
            newList.push_back(list[i]);
        }
        return newList;
    }
};

// Please keep the following test cases
int main() {
    FunctionalList<int> intList;
    intList.add(1);
    intList.add(2);
    intList.add(3);

    cout << "Integer List:\n";
    cout << "Head: " << intList.head() << endl;
    cout << "Tail: [ ";
    for (auto element : intList.tail()) {
        cout << element << " ";
    }
    cout << "]" << endl;
    cout << "Init: [ ";
    for (auto element : intList.init()) {
        cout << element << " ";
    }
    cout << "]" << endl;
    cout << "Last: " << intList.last() << endl;

    FunctionalList<string> stringList;
    stringList.add("apple");
    stringList.add("banana");
    stringList.add("orange");

    cout << "\nString List:\n";
    cout << "Head: " << stringList.head() << endl;
    cout << "Tail: [ ";
    for (auto element : stringList.tail()) {
        cout << element << " ";
    }
    cout << "]" << endl;
    cout << "Init: [ ";
    for (auto element : stringList.init()) {
        cout << element << " ";
    }
    cout << "]" << endl;
    cout << "Last: " << stringList.last() << endl;

    return 0;
}

/*
Integer List:
Head: 1
Tail: [ 2 3 ]
Init: [ 1 2 ]
Last: 3

String List:
Head: apple
Tail: [ banana orange ]
Init: [ apple banana ]
Last: orange
*/