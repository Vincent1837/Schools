#include "anduin.h"
#include "battle.h"
#include "io.h"

Anduin::Anduin(Battle* battle): Hero("Anduin", 0, 0, 0, battle) {}

Anduin::~Anduin() {}

void Anduin::action() {
    displayText(this->battle, this->name + " 's turn.");
    pressEntertoContinue();
}