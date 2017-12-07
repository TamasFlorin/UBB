package Model.Statement;

import Model.Expression.ExpressionException;
import Model.Expression.IExpression;
import Model.State.ProgramState;
import Util.Stack.MyIStack;
import Util.Stack.StackException;

public class WhileStatement implements IStatement {
    private final IExpression expression;

    public WhileStatement(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState programState) throws ExpressionException, StatementException {
        MyIStack<IStatement> stack = programState.getExecutionStack();

        int value = expression.evaluate(programState.getSymbolTable(),programState.getHeap());

        if( value != 0) {
            try {
                IStatement second = stack.top();
                stack.push(this);
                stack.push(second);
            }catch (StackException e){
                throw new StatementException(e.getMessage());
            }
        }else {
            try {
                stack.pop();
            }catch (StackException e){
                throw new StatementException(e.getMessage());
            }
        }

        return programState;
    }

    @Override
    public String toString() {
        return "While(" + this.expression + ")";
    }
}
