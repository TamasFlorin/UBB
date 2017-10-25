package Model.Statement;

import Model.Expression.ExpressionException;
import Model.Expression.IExpression;
import Model.State.ProgramState;
import Util.Dictionary.MyIDictionary;

public class AssignmentStatement implements IStatement {
    private String variable;
    private IExpression expression;

    public AssignmentStatement(String variable, IExpression expression){
        this.variable = variable;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState programState) throws ExpressionException {
        MyIDictionary<String,Integer> symbolTable = programState.getSymbolTable();

        int result = this.expression.evaluate(symbolTable);

        // update the value of the variable
        symbolTable.put(this.variable,result);

        return programState;
    }

    @Override
    public String toString() {
        return "("+ this.variable + "=" + this.expression+")";
    }
}
