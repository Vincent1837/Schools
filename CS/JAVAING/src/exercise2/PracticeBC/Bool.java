package exercise2;

public class Bool extends Exp{

    private boolean booleanVal;

    public Bool (boolean b) {
        this.booleanVal = b;
    }

    public boolean eval() {
        return this.booleanVal;
    }

    public String toSExp() {
        if (this.booleanVal) {
            return "T";
        } else {
            return "F";
        }
    }
}

