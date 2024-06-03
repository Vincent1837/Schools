#include <iostream>
#include <string>
#include <array>

using namespace std;

// Define a template structure calculates the Nth element of the Fibonacci number
template<int N>
struct Fibonacci {
    static const int value = Fibonacci<N-1>::value + Fibonacci<N-2>::value;
};

template<>
struct Fibonacci<1> {
    static const int value = 1;
};

template<>
struct Fibonacci<2> {
    static const int value = 1;
};

// Define a Cage template class
template<int N>
class Cage {
private:
    std::array<std::string, Fibonacci<N>::value> rabbitNames;
    std::string cageName;

public:
    Cage() : cageName("Rabbit" + std::to_string(Fibonacci<N>::value)) {
        rabbitNames.fill("");
    }

    void addRabbit(const std::string& name, const int& index) {
        if (index >= 0 && index < Fibonacci<N>::value) {
            rabbitNames[index] = cageName + "-" + name;
        }
    }

    void displayRabbits() const {
        std::cout << "Rabbits in cage " << cageName << ":" << std::endl;
        bool hasRabbit = false;
        for (const auto& name : rabbitNames) {
            if (name.empty()) {
                std::cout << "no rabbit" << std::endl;
            } else {
                std::cout << name << std::endl;
                hasRabbit = true;
            }
        }
    }
};

int main() {
    Cage<3> cageA;
    cageA.addRabbit("Bug", 0);
    cageA.addRabbit("Cry", 1);
    cageA.displayRabbits();
    
    cout << endl;
    
    Cage<6> cageB;
    cageB.addRabbit("HAPPY", 1);
    cageB.addRabbit("ALL", 3);
    cageB.addRabbit("PASS", 5);
    cageB.addRabbit("BYE", 7);
    cageB.displayRabbits();
    return 0;
}
/*
C.
Rabbits in cage Rabbit2:
Rabbit2-Bug
Rabbit2-Cry

Rabbits in cage Rabbit8:
no rabbit
Rabbit8-HAPPY
no rabbit
Rabbit8-ALL
no rabbit
Rabbit8-PASS
no rabbit
Rabbit8-BYE
*/