package Model.Expression;

import Util.Dictionary.MyIDictionary;

public class ConstantExpression implements IExpression {
    private int value;

    public ConstantExpression(int value){
        this.value = value;
    }

    @Override
    public int evaluate(MyIDictionary<String,Integer> symbolTable) throws ExpressionException {
        return this.value;
    }

    @Override
    public String toString() {
        return "(" + this.value + ")";
    }
}
