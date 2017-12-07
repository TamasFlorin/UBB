package Util.Tuple;

public class Tuple<X,Y> {
    private final X first;
    private final Y second;

    public Tuple(X first,Y second){
        this.first = first;
        this.second = second;
    }

    public X getFirst() {
        return first;
    }

    public Y getSecond() {
        return second;
    }

    @Override
    public String toString() {
        return "(" + this.first + ";" + this.second + ")";
    }
}
