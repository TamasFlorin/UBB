package Model.Expression;

import Util.Dictionary.MyIDictionary;
import Util.Heap.IHeap;

public class LessOrEqualExpression implements IExpression {
    private final IExpression left;
    private final IExpression right;

    public LessOrEqualExpression(IExpression left,IExpression right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public int evaluate(MyIDictionary<String, Integer> symbolTable, IHeap heap) throws ExpressionException {
        int leftValue = this.left.evaluate(symbolTable,heap);
        int rightValue = this.right.evaluate(symbolTable,heap);

        if( leftValue <= rightValue)
            return 1;

        return 0;
    }

    @Override
    public String toString() {
        return "( " + this.left + " <= " + this.right + ")";
    }
}
