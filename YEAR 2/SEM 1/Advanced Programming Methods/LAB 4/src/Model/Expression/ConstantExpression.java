package Model.Expression;

import Util.Dictionary.MyIDictionary;
import Util.Heap.IHeap;

public class ConstantExpression implements IExpression {
    private int value;

    public ConstantExpression(int value){
        this.value = value;
    }

    @Override
    public int evaluate(MyIDictionary<String,Integer> symbolTable, IHeap heap) throws ExpressionException {
        return this.value;
    }

    @Override
    public String toString() {
        return "(" + this.value + ")";
    }
}
