<font face="Times New Roman">

# Discrete Mathematics Homework1
  
## Section 1-1

 **6 . Suppose that Smartphone A has 256 MB RAM and 32 GB ROM, and the resolution of its camera is 8 MP ; Smartphone B has 288 MB RAM and 64 GB ROM, and the resolution of its camera is 4 MP; and Smartphone C has 128 MB RAM and 32 GB ROM, and the resolution of its camera is 5 MP. Determine the truth value of each of these propositions.**

- (a) <font color = "red">False</font> (b) <font color = "blue">True</font> (c) <font color = "red">False</font> (d) <font color = "red">False</font> (e) <font color = "red">False</font>

**10 . Let p and q be the propositions “The election is decided” and “The votes have been counted,” respectively. Express each of these compound propositions as an English sentence.**

- (a) $\neg{p}$ : ***The election is not dicided.***
- (b) $p \lor{q}$ : ***The election is decided or the votes have been counted.***
- (c) $\neg{p} \land{q}$ : ***The election is not dicided and the votes have been couted.***
- (d) $q \to p$ : ***If the votes have been counted, the election is decided.***
- (e) $\neg{q} \to \neg{p}$ : ***If the votes have not been counted, the election is not be decided.***
- (f) $\neg{p} \to \neg{q}$ : ***If the election is not decided, then the votes have not been counted.***
- (g) $p \leftrightarrow{q}$ : ***The election will be decided if and only if the votes have been counted.***
- (h) $\neg{q}\lor{}(\neg{p}\land{q})$ : ***The election is not decided and the votes have been counted, or the votes haven't been counted.***

**28 . State the converse, contrapositive, and inverse of each of these conditional statements.**  

- (a) If it snows tonight, then I will stay at home.
  - converse : ***If I stay at home, it will snow tonight.***
  - contrapositive : ***If I don't stay at home, it won't snow tonight.***
  - inverse : ***I won't stay at home if it doesn't snow tonight.***
- (b) I go to the beach whenever it is a sunny summer day.
  - converse : ***It is a sunny summer day whenever I go to the beach.***
  - contrapositive : ***It is not a sunny summer day whenever I don't go to the beach.***
  - inverse : ***I don't go to the beach whenever it isn't a sunny summer day.***
- (c) When I stay up late, it is necessary that I sleep until noon.
  - converse : ***When I sleep until noon, it is necessary that I stay up late.***
  - contrapositive : ***When I don't sleep until noon, it is necessary that I don't stay up late.***
  - inverse : ***When I don't stay up late, it is necessary that I don't sleep until noon.***

## Section 1-2

**10 . Are these system specifications consistent? “Whenever the system software is being upgraded, users cannot access the file system. If users can access the file system,then they can save new files. If users cannot save new files, then the system software is not being upgraded.”**
- ***Let $p, q, r$ represent "The system software is being upgraded.", "Users can access the file system."and "Users can save new files." respectively, then the sentences can be translated to :***  

> $p \to \neg{q}$ : “Whenever the system software is being upgraded, users cannot access the file system."  

> $q \to r$ : "If users can access the file system,then they can save new files."  

> $\neg{r} \to \neg{p}$ : "If users cannot save new files, then the system software is not being upgraded."  

1. ***Assume that $\neg{r}$ is true, then $\neg{p}$ is also true.***
2. ***Since $r$ is false, $q$ must be false.***
- ***When $p, q, r$ are false, all three propositions are true, so they are consistent.***

**20 . A says “The two of us are both knights” and B says “A is a knave."**
- ***If A is a knight, then B will also be a knight. In that case, both of them are telling the truth ,which means A is a knight and a knave. That is a contradiction. So A is a knave and B is a knight, bcause B is telling the truth.***

## Section 1-3

**8 . Use De Morgan’s laws to find the negation of each of the following statements.**
- (a) Kwame will take a job in industry or go to graduate school.  
  > $\neg{}(p\lor{q})\equiv (\neg{p} \land \neg{q})$
  - ***Kwame won't tkae a job in industry, and he won't go to graduate school either.***
- (b) Yoshiko knows Java and calculus.  
  > $\neg{}(p\land{q})\equiv (\neg{p} \lor \neg{q})$
  - ***Yoshiko doesn't know Java ,or he/she doesn't know calculus***
- (c) James is young and strong.  
  > $\neg{}(p\land{q})\equiv (\neg{p} \lor \neg{q})$
  - ***James is not young, or he is not strong.***
- (d) Rita will move to Oregon or Washington.  
  > $\neg{}(p\lor{q})\equiv (\neg{p} \land \neg{q})$
  - ***Rita will not move to Oregon, and she will not move to Washington either.***

**14 . Deterimin whether $(\neg{p}\land(p\to{q}))\to \neg{q}$ is a tautology.**
- $(\neg{p}\land(p\to{q}))\to \neg{q} \equiv \neg{(\neg{p}\land(p\to{q}))}\lor \neg{q}$
$\equiv{}\neg{(\neg{p}\land(\neg{p}\lor{q}))}\lor \neg{q}$
$\equiv{}\neg{(\neg{p})}\lor\neg{(\neg{p}\lor{q)}}\lor \neg{q}$
$\equiv{}p\lor(\neg{(\neg{p})}\land\neg{q})\lor\neg{q}$
$\equiv{}p\lor(p\land\neg{q})\lor\neg{q}$
$\equiv{}(p\lor\neg{q})\lor(p\land\neg{q})$
$\equiv{}((p\lor\neg{q})\lor p)\land((p\lor\neg{q})\lor\neg{q})$
$\equiv{}(p\lor\neg{q})\land(p\lor\neg{q})$
$\equiv{p\lor\neg{q}}$
  ***The compoud proposition is false when $p$ is false and $\neg{q}$ is also false.
  So it's not a tautology.***

**36 . When does *s\* =s* ,where *s* is a compound proposition?**
- $s:p\land T;p\lor F$

## Section 1-4

**8 . Translate these statements into English, where $R(x)$ is “x is a rabbit” and $H(x)$ is “x hops” and the domain consists of all animals**
- (a) $\forall{x}(R(x)\to H(x))$
  - ***If an animal is a rabbit, then it hops.***
- (c) $\exists{x}(R(x)\to H(x))$
  - ***There exist an animal such that if it's a rabbit, then it hops.***

**14 . Determine the truth value of each of these statements if the domain consists of all real numbers.**
- (b) $\exists{x}(x^4\lt x^2)$ : <font color = "blue">True</font>
  - $0\le x\le 1\to (x^4\lt x^2)$
- (d) $\forall{x}(2x\gt x)$ : <font color = "red">False</font>
  - $x\le 0\to (2x\le x)$

**22 . For each of these statements find a domain for which the statement is true and a domain for which the statement is false.**
- (b) There is someone older than 21 years.
  - <font color = "blue">True</font> : ***If the domain is all the people in Taiwan.***
  - <font color = "red">False</font> : ***If the domain is all the 20-year-old people.***
- (d) Someone knows more than two other people.
  - <font color = "blue">True</font> : ***If the domain is all the people in a middle school.***
  - <font color = "red">False</font> : ***If the domain is a group of people who just met.***

**34 . Express the negation of these propositions using quantifiers, and then express the negation in English**
- (a) ***For all drivers, they obey the speedlimit.***
- (c)***There exist a person who can keep a secret in the domain of all the people.***

**46 . Establish these logical equivalences, where $x$ does not occur as a free variable in A. Assume that the domain is nonempty**
- (a) $(\forall{x}P(x))\lor A\equiv \forall{x}(P(x)\lor A)$
- (b) $(\exists{x}P(x))\lor A\equiv \exists{x}(P(x)\lor A)$

**50 . Show that $\forall{x}P(x)\lor\forall{x}Q(x)$ and $\forall{x}(P(x)\lor Q(x))$ are not logically equivalent.**
- ***Let $P(x)$ represent "$x$ is less than or equal to 0.", and let $Q(x)$ represent "$x$ is greater than 0." Assume that the domain is the real number, then the first proposition will be false, and the second proposition will be true.  
That's because for all the real number $x$, $x$ is ether positive or negetive, or 0. But neither all the real number $x$ are negetive nor all the real number $x$ are positive.  
So the two propositions are not logically equivalent.***
  
## Section 1-5

**12 . Let $I(x)$ be the statement “$x$ has an Internet connection”and $C(x, y)$ be the statement “$x$ and $y$ have chatted over the Internet” where the domain for the variables $x$ and $y$ consists of all students in your class. Use quantifiers to express each of these statements.**
- (a) Jerry does not have an Internet connection.
  - $\neg{I(Jerry)}$ 
- (d) No one in the class has chatted with Bob.
  - $\neg{}\exists{x}C(x, Bob)$
- (g) Not everyone in your class has an Internet connection
  - $\neg{}\forall{x}I(x)$
- (j) Everyone in your class with an Internet connection has chatted over the Internet with at least one other student in your class.
  - $\forall{x}\exists{y}(I(x)\to C(x, y)\land{}(x\neq{y}))$
- (m) There is a student in your class who has chatted with everyone in your class over the Internet
  - $\exists{x}\forall{y}C(x, y)$

**20 . Express each of these statements using predicates, quantifiers, logical connectives, and mathematical operators where the domain consists of all integers.**
- (a) The product of two negative integers is positive.
  - $\forall{x}\forall{y}((x\lt{0})\land(y\lt{0})\to (xy\gt{0}))$
- (b) The average of two positive integers is positive.
  - $\forall{x}\forall{y}((x\gt{0})\land(y\gt{0})\to (\frac{x+y}{2}\gt{0}))$
- (c) The difference of two negative integers is not necessarily negative.
  - $\exists{x}\exists{y}((x\lt{0})\land(y\lt{0})\to(x-y\geq{0}))$
- (d) The absolute value of the sum of two integers does not exceed the sum of the absolute values of these integers.
  - $\forall{x}\forall{y}(|x+y|\leq|x|+|y|)$

**28 . Determine the truth value of each of these statements if the domain of each variable consists of all real numbers.**
- (a) $\forall{x}\exists{y}(x^2=y)$ : <font color = "blue">True</font>
  - $y = x^2\in{\mathbb{R}}$
- (d) $\exists{x}\exists{y}(x+y\neq y+x)$ : <font color = "red">False</font>
  - ***commutative law holds in real numbers***
- (g) $\forall{x}\exists{y}(x+y=1)$ : <font color = "blue">True</font>
  - $y=1-x\in\mathbb{R}$

**40 . Find a counterexample, if possible, to these universally quantified statements, where the domain for all variables consists of all integers**
- (a) $\forall{x}\exists{y}(x=\frac{1}{y})$
  - ***counterexample :***  $x=2$
- (b) $\forall{x}\exists{y}(y^2-x\lt{100})$
  - ***counterexample :*** $x=-101$
- (c) $\forall{x}\forall{y}(x^2\neq y^3)$
  - ***counterexample :*** $x=8$

## Section 1-6

**12 . Show that the argument form with premises $(p\land{t})\to(r\lor{s}), q\to(u\land{t}), u\to{p}$ and $\neg{s}$ and conclusion $q\to r$ is valid by first using Exercise 11 and then using rules of inference from Table 1.**
- ***If we can proof that that the argument form with premises $(p\land{t})\to(r\lor{s}), q\to(u\land{t}), u\to{p}, \neg{s}$ and $q$, and conclusion $r$ is valid, then the argument in the question will also be valid(Ex.11).***
- (1) $q\to(u\land{t})$ (permise)
  (2) $q$ (permise)
  (3) $u\land{t}$ (modus ponens using (1), (2))
  (4) $u$ (simplification using (3))
  (5) $t$ (simplification using (3))
  (6) $u\to{p}$ (permise)
  (7) $p$ (modus ponens using (4), (6))
  (8) $p\land{t}$ (conjuction using (5), (7))
  (9) $(p\land{t})\to(r\lor{s})$ (permise)
  (10) $r\lor{s}$ (modus ponens using (8), (9))
  (11) $\neg{s}$ (permise)
  ___
  ∴ $r$ (disjuctive syllogism using (10), (11))
- ***Therefore, all the arguments above are valid.***

**20 . Determine whether these are valid arguments.**
- (a) If $x$ is a positive real number, then $x^2$ is a positive real number. Therefore, if $a^2$ is positive, where $a$ is a real number, then $a$ is a positive real number.
  - <font color = "red">Invalid</font> : ***Fallacy of affirming the conclusion.***
- (b) If $x^2\neq{0}$, where $x$ is a real number, then $x\neq{0}$. Let $a$ be a real number with $a^2\neq{0}$; then $a\neq{0}$.
  - <font color = "blue">Valid</font> : ***Universal instantiaion.***

**28 . Use rules of inference to show that if $\forall{x}(P(x)\lor Q(x))$ and $\forall{x}((\neg{P(x)}\land Q(x))\to{R(x)})$ are true, then $\forall{x}(\neg{R(x)}\to P(x))$ is also true, where the domains of all quantifiers are the same.**
- (1) $\forall{x}(P(x)\lor Q(x))$ (permise)
  (2) $\forall{x}(P(x)\lor Q(x)\lor R(x))$ (addition using (1))
  (3) $\forall{x}((\neg{P(x)}\land Q(x))\to R(x))$ (permise)
  (4) $\forall{x}(\neg(\neg{P(x)}\land Q(x))\lor R(x))$ (logical equivalence of (3))
  (5) $\forall{x}({P(x)}\lor \neg Q(x)\lor R(x))$ (De morgan's law using (4))
  (6) $\forall{x}((P(x)\lor R(x))\lor(P(x)\lor R(x)))$ (resolution using (2), (5))
  (7) $\forall{x}(P(x)\lor R(x))$ (logical equivalence of (6))
  ___
  ∴ $\forall{x}(\neg{R(x)}\to P(x))$ (logical equivalence of (7))

## Section 1-7

**10 . Use a direct proof to show that the product of two rational numbers is rational.** 
- $\forall{r, s, t, u}(((r, s, t, u)\in\mathbb{Z})\land (su\neq{0}) \to (\frac{r}{s}\in\mathbb{Q})\land(\frac{t}{u}\in\mathbb{Q}))$ 
  $\forall{r, s, t, u}((rt\in\mathbb{Z})\land(su\in\mathbb{Z})\land(su\neq{0})\to(\frac{rt}{su}\in\mathbb{Q}))$
  $\forall{n, m}((n=\frac{r}{s})\land (m=\frac{t}{u}) \to (nm=\frac{rt}{su}))$
  ***By the definition of the rational nuber, we can conclude that :***
  $\forall{n, m}((n\in\mathbb{Q})\land(m\in\mathbb{Q})\to(nm\in\mathbb{Q}))$

**16 . Prove that if $m$ and $n$ are integers and $mn$ is even, then $m$ is even or $n$ is even.**
- ***Proof by contraposition:***
  ***Let $m$ be odd and $n$ be odd, that maens $m=2i+1$ and $n=2j+1$, where $i, j$ are some integers.***
  ***Then $mn=(2i+1)\times(2j+1)=4ij+2(i+j)+1=2(2ij+i+j)+1$***
  ***Because $(2ij+i+j)$ is an integer , $mn$ is an odd integer.***
  ***We have shown : "If $m$ and $n$ are odd integers, then $mn$ is also an odd integer.", which is logically equivalent to the statment "If $m$ and $n$ are integers and $mn$ is even, then $m$ is even or $n$ is even." because an integer is either even or odd.***

**24 . Show that at least 3 of any 25 days chosen must fall in the same month of the year.**
- ***If there were at most two days in a same month, then we could have two days fall in each month of a year in the total of 24 days. From that, if we wanted to choose another day in that year, then that extra day would fall in one of the twelve months in that year. Which leads to a month where the extra chosen day falls having 3 chosen days.***

## Section 1-8

**10 . Prove that either $2\cdot 10^{500}+15$ or $2\cdot 10^{500}+16$ is not a perfect square. Is your proof constructive or nonconstructive?**
- ***The difference between two consecutive perfect squares is the sum of the squareroots of the two numbers. So the only two perfect squares that deffer by one is 0 and 1. Therefore, at least one of the two numbers will not be a perfect square, since they have are "too close" to each other.***
- ***This is a nonconstructive proof because we don't actually know the actuall values of them, so we can't be sure of that what number is not a perfect square.***

**20 . Prove that given a real number $x$ there exist unique numbers $n$ and $\epsilon$ such that $x=n+\epsilon, n$ is an integer, and $0\leq{\epsilon}\lt{1}$.**
- ***Let $n=\lfloor{x}\rfloor,$we 'll get $x-1\lt{n}\leq{x}$, and then $(\epsilon = x-n)$ so that $0\leq{\epsilon}\lt{1}$, therefore $\epsilon$ is unique to $n$ and $n$ must be unique as well, since any other choice of integer $n$ will cause $\epsilon$ to be out of range$[0,1)$.***

## Section 2-1

**26 . Show that if $A\subseteq{C}$ and $B\subseteq{D}$, then $A\times{B}\subseteq C\times{D}$.**
- $\forall{a, b}((a\in{A})\land(b\in{B})\to((a, b)\in(A\times{B})))$
  $\forall{a}((a\in{A})\land(A\subseteq{C})\to(a\in{C}))$
  $\forall{b}((b\in{B})\land(B\subseteq{D})\to(b\in{D}))$
  $\forall{a, b}((a, b)\in(C\times{D}))$
  therefore $A\times{B}\subseteq C\times{D}$

## Section 2-2

**18 . Let $A,B,$ and $C$ are sets. Show that**
- (a) $(A\cup{B})\subseteq(A\cup{B}\cup{C}).$
  - ***Soppose that $x\in(A\cup{B})$ ,which means that $x$ is either in $A$ or in $B$. In either case, $x\in(A\cup{B}\cup{C})$***
  
- (c) $(A-B)-C\subseteq A-C.$
  - ***Soppose that $x\in(A-B)-C$ ,which means that $x$ is in $A$ but is in neither $B$ nor $C$. This certainly contains all the elements $x$ that is in $A$ but is not in $C$.***
- (e) $(B-A)\cup(C-A)=(B\cup{C}-A).$
  - proof of : $(B-A)\cup(C-A)\subseteq(B\cup{C}-A).$
    - ***Soppose that $x\in(B-A)\cup(C-A)$, which means that $x$ is in $B-A$ or $x$ is in $C-A$.***
    ***If $x$ is in $B-A$, then $x$ is in $B$ but is not in $A$, and if so, $x$ is in $B\cup{C}$ but is not in $A$.*** 
    ***If $x$ is in $C-A$, then $x$ is in $C$ but is not in $A$, and if so, $x$ is in $B\cup{C}$ but is not in $A$.***
  - proof of : $(B\cup{C}-A)\subseteq(B-A)\cup(C-A)$
    - ***Soppose that $x\in(B\cup{C}-A)$, which means that $x\in(B\cup{C})$ and $x\notin{A}$ .This tells us that $x$ is either in $B$ or in $C$. Thus either $x$ in $B-A$ or $x$ in $C-A$, in either case, $X\in(B-A)\cup(C-A)$***

**38 . Show that if $A$ and $B$ are sets, then**
- (a) $A\oplus{B}=B\oplus{A}$
  - ***OBVIOUSLY!!!!!!!!IT IS SO SYMMETRIC!!(symmetric difference)***
- (b) $(A\oplus{B})\oplus{B}=A$
  - ***Soppose $x\in(A\oplus{B})\oplus{B}$, then two case.***
    1. ***If $x$ is not in $B$, then $x\in(A\oplus{B})$, and if so, then x must be in $A-{B}$***
    2. ***If $x$ is not in $A\oplus{B}$, then $x\in{B}$, and if so, then $x$ must be in $A\cap{B}$*** 
    3. ***Either the case $x$ will be in $A$***
  - ***Soppose $x \in A$, then when $x$ in $B$, $x\notin{A\oplus{B}}$***

**48 . Let $A_i=\{... ,-2, -1, 0, 1, 2, 3, ..., i\}$ Find**
- (a) $\bigcup\limits_{i=1}^{n}A_i = A_n$
- (b) $\bigcap\limits_{i=1}^{n}A_i = A_1$

## Section 2-3

**6 . Find the domain and range of these functions.**
- (a) the function that assigns to each pair of positive integers the first integer of the pair
  - Domain : $\Z^+\times\Z^+$
  - Range : $\Z^+$
- (c) the function that assigns to a bit string the number of ones minus the number of zeros in the string
  - Domain : ***All bit strings***
  - Range : $\Z$
- (e) the  function  that  assigns  to  a  bit  string  the  longest string of ones in the string
  - Domain : ***All bit strings***
  - Range : $\{1, 11, 111, 1111,......\}$

**22 . Determine whether each of these functions is a bijection from $\R$ to $\R$.**
- (a) $f(x)=-3x+4$
  - <font color="blue">Yes</font> : $f^{-1}(x)=\frac{4-x}{3}$.
- (b) $f(x)=-3x^2+7$
  - <font color="red">No</font> : ***It is not one-on-one***.
- (c) $f(x)=\frac{x+1}{x+2}$
  - <font color="red">No</font> : ***The domain and the range are not $\R$***.
- (d) $f(x)=x^5+1$
  - <font color="blue">Yes</font> : $f^{-1}(x)=\sqrt[5]{x-1}$.

**38 . Let $f(x)=ax+b$ and $g(x)= cx+d$ , where $a, b, c,$ and $d$ are constants. Determin necessary and sufficient conditions on the constants $a, b, c,$ and $d$ so that $f\circ{g}=g\circ{f}$.**
- $(f\circ{g})(x)=acx+ad+b$ , $(g\circ{f})(x)= cax+cb+d$
  ***They are equal if $ad+b=cb+d$***
  ***Therefore*** $\forall{a, b, c, d}((ad+b=cb+d)\to (f\circ{g}=g\circ{f}))$

**54 . Prove that if $x$ is a real number, then $\lfloor{-x}\rfloor=-\lceil{x}\rceil$ and $\lceil{-x}\rceil=-\lfloor{x}\rfloor$.**
- proof of $\lfloor{-x}\rfloor=-\lceil{x}\rceil$ : 
  - ***Let $x=n-\epsilon$, where $n$ is an integer and $0\leq\epsilon\lt{1}$, in that case $\lceil{x}\rceil=n$.***
    ***Therefore $\lfloor{-x}\rfloor=\lfloor{-n+\epsilon}\rfloor=-n=-\lceil{x}\rceil$.***
- proof of $\lceil{-x}\rceil=-\lfloor{x}\rfloor$
  - ***Let $x=n+\epsilon$, where $n$ is an integer and $0\leq\epsilon\lt{1}$, in that case $\lfloor{x}\rfloor=n$.***
    ***Therefore $\lceil{-x}\rceil=\lceil{-n-\epsilon}\rceil=-n=-\lfloor{x}\rfloor$.***
</font>
