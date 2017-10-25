package Model.Expression;

import Util.Dictionary.MyIDictionary;

public interface IExpression {
    int evaluate(MyIDictionary<String,Integer> symbolTable) throws ExpressionException;
}
