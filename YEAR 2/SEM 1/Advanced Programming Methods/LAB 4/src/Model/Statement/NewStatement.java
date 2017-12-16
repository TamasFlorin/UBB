package Model.Statement;

import Model.Expression.ExpressionException;
import Model.Expression.IExpression;
import Model.State.ProgramState;
import Util.Dictionary.MyIDictionary;

import java.io.IOException;

public class NewStatement implements IStatement {
    private String variableName;
    private IExpression expression;

    public NewStatement(String variableName,IExpression expression) {
        this.variableName = variableName;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState programState) throws ExpressionException, StatementException {
        MyIDictionary<String,Integer> symbolTable = programState.getSymbolTable();

        int value = this.expression.evaluate(symbolTable,programState.getHeap());

        // allocate space on the heap and get it's address
        int address = programState.getHeap().allocate(value);

        // set the address of the variable
        symbolTable.put(this.variableName,address);

        return null;
    }

    @Override
    public String toString() {
        return "NewStatement(" + this.variableName + "," + this.expression + ")";
    }
}
