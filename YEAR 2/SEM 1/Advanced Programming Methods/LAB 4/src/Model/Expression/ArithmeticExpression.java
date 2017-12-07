package Model.Expression;

import Util.Dictionary.MyIDictionary;
import Util.Heap.IHeap;

public class ArithmeticExpression implements IExpression {
    private char operator;
    private IExpression operand1,operand2;

    public ArithmeticExpression(char operator, IExpression operand1, IExpression operand2){
        this.operator = operator;
        this.operand1 = operand1;
        this.operand2 = operand2;
    }

    @Override
    public int evaluate(MyIDictionary<String,Integer> symbolTable,IHeap heap) throws ExpressionException{
        int first = this.operand1.evaluate(symbolTable,heap);
        int second = this.operand2.evaluate(symbolTable,heap);

        switch(this.operator) {
            case '+': return first + second;
            case '-': return first - second;
            case '*': return first * second;
            case '/':
                if(second == 0)
                    throw new ExpressionException("Division by 0!");
                return first / second;
            default: throw new ExpressionException("Invalid operator!");
        }
    }

    @Override
    public String toString() {
        return "(" + operand1 + operator + operand2 + ")";
    }
}
