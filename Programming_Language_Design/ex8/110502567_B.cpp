#include <iostream>
#include <typeinfo>

using namespace std;

class Shape {
public:
    virtual ~Shape() {}
};
class Circle : public Shape {
public:
    void draw() const { cout << "Drawing a Circle" << endl; }
};
class Rectangle : public Shape {
public:
    void draw() const { cout << "Drawing a Rectangle" << std::endl; }
};

// Define a function identifyAndDraw to identify the type of the object, and then calls the draw method
void identifyAndDraw(Shape* shape) {
    if (typeid(*shape) == typeid(Circle)) {
        cout << "This is a Circle" << endl;
        dynamic_cast<Circle*>(shape)->draw();
    } else if (typeid(*shape) == typeid(Rectangle)) {
        cout << "This is a Rectangle" << endl;
        dynamic_cast<Rectangle*>(shape)->draw();
    } else {
        cout << "Unknown Shape" << endl;
    }
}

int main() {
    Shape* shape1 = new Circle;
    Shape* shape2 = new Rectangle;
    Shape* shape3 = new Shape;
    identifyAndDraw(shape1);
    identifyAndDraw(shape2);
    identifyAndDraw(shape3);
    delete shape1;
    delete shape2;
    delete shape3;
    return 0;
}

/*
This is a Circle
Drawing a Circle
This is a Rectangle
Drawing a Rectangle
Unknown Shape
*/