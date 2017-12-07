package Model.Statement;

import Model.Expression.ExpressionException;
import Model.Expression.IExpression;
import Model.State.ProgramState;
import Util.List.MyIList;

public class PrintStatement implements IStatement {
    private IExpression expression;

    public PrintStatement(IExpression expression) {
        this.expression = expression;
    }
    
    @Override
    public String toString() {
        return "print(" + expression + ")";
    }

    @Override
    public ProgramState execute(ProgramState state) throws ExpressionException {
        int result = expression.evaluate(state.getSymbolTable(),state.getHeap());
        MyIList<Integer> output = state.getOutput();

        output.add(result);

        // this needs to be removed from here
        //System.out.println(result);

        return state;
    }
}
