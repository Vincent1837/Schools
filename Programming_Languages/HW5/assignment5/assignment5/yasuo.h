#ifndef __YASUO_H
#define __YASUO_H
#include "hero.h"
#include "monster.h"

class Battle;

class Yasuo: public Hero {
private:

public:
    Yasuo(Battle* Battle);
    ~Yasuo();
    void action();
};

#endif