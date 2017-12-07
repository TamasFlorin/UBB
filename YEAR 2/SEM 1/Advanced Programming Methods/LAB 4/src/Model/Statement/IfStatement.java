package Model.Statement;

import Model.Expression.ExpressionException;
import Model.Expression.IExpression;
import Model.State.ProgramState;
import Util.Stack.MyIStack;

public class IfStatement implements IStatement {
    private IExpression expression;
    private IStatement thenStatement;
    private IStatement elseStatement;

    public IfStatement(IExpression expression, IStatement thenS, IStatement elseS){
        this.expression = expression;
        this.thenStatement = thenS;
        this.elseStatement = elseS;
    }

    @Override
    public ProgramState execute(ProgramState programState) throws ExpressionException {
        int result = this.expression.evaluate(programState.getSymbolTable(),programState.getHeap());

        MyIStack<IStatement> executionStack = programState.getExecutionStack();

        if( result != 0) { // true
            executionStack.push(this.thenStatement);
        }
        else
            executionStack.push(this.elseStatement); // false

        return programState;
    }

    @Override
    public String toString() {
        return "(" + "IF " + expression + " THEN " + thenStatement + " ELSE " + elseStatement + ")";
    }
}
