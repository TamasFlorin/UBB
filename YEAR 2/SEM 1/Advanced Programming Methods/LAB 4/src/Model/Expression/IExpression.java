package Model.Expression;

import Util.Dictionary.MyIDictionary;
import Util.Heap.IHeap;

public interface IExpression {
    int evaluate(MyIDictionary<String,Integer> symbolTable, IHeap heap) throws ExpressionException;
}
