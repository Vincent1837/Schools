package exercise2;

public class Not extends Exp {
    private Exp e;

    public Not (Exp exp) {
        this.e = exp;
    }

    public boolean eval () {
        return !this.e.eval();
    }

    public String toSExp () {
        return "[not " + e.toSExp() + "]";
    }
}
