#include <typeinfo>
#include <iostream>

class Base {
public:
    virtual ~Base() {}  // Virtual destructor ensures presence of vtable
};
class Derived : public Base {
public:
    void sayHello() { std::cout << "Hello from Derived" << std::endl; }
};

int main() {
    Base* base = new Derived;
    const std::type_info& typeInfoBase = typeid(*base);
    
    std::cout << "Type of base: " << typeInfoBase.name() << std::endl;
    std::cout << "Type of Derived: " << typeid(Derived).name() << std::endl;
    
    if (typeInfoBase == typeid(Derived))
        std::cout << "base is of type Derived" << std::endl;

    delete base;
    return 0;
}