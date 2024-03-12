package exercise2;

// Main.java
public class Main {
	public static void main(String[] args) {
		Exp[] practiceB = {
				new Bool(true),
				new Bool(false),
				new Not(new Bool(false)),
				new And(new Bool(true), new Bool(false)),
				new Or(new Bool(true), new Bool(false)),
				new Or(new Bool(true), new And(new Bool(true), new Bool(false)))
		};
		for(Exp e : practiceB) System.out.println(e.toSExp());
	}
}
/*
output:
T
F
[not F]
[and T F]
[or T F]
[or T [and T F]]
*/