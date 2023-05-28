#include "yasuo.h"
#include "battle.h"
#include "io.h"

Yasuo::Yasuo(Battle* battle): Hero("Yasuo", 0, 0, 0, battle) {}

Yasuo::~Yasuo() {}

void Yasuo::action() {
    displayText(this->battle, this->name + " 's turn.");
    pressEntertoContinue();
    
}