#ifndef __ANDUIN_H
#define __ANDUIN_H
#include "hero.h"
#include "monster.h"

class Battle;

class Anduin: public Hero {
private:

public:
    Anduin(Battle* Battle);
    ~Anduin();
    void action();
};

#endif