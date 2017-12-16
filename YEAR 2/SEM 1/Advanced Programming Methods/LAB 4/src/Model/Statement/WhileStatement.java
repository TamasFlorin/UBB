package Model.Statement;

import Model.Expression.ExpressionException;
import Model.Expression.IExpression;
import Model.State.ProgramState;
import Util.Stack.MyIStack;
import Util.Stack.StackException;

public class WhileStatement implements IStatement {
    private final IExpression expression;
    private final IStatement statement;

    public WhileStatement(IExpression expression,IStatement statement) {
        this.expression = expression; this.statement = statement;
    }

    @Override
    public ProgramState execute(ProgramState programState) throws ExpressionException, StatementException {
        MyIStack<IStatement> stack = programState.getExecutionStack();

        int value = expression.evaluate(programState.getSymbolTable(),programState.getHeap());

        if( value == 0) {
            return programState;
        }

        stack.push(this);
        stack.push(this.statement);

        return null;
    }

    @Override
    public String toString() {
        return "While(" + this.expression + ")";
    }
}
