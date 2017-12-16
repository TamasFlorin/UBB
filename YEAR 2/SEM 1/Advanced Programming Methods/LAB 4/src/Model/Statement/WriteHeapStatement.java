package Model.Statement;

import Model.Expression.ExpressionException;
import Model.Expression.IExpression;
import Model.State.ProgramState;
import Util.Dictionary.MyIDictionary;
import Util.Heap.HeapException;

public class WriteHeapStatement implements IStatement {
    private final String variableName;
    private final IExpression expression;

    public WriteHeapStatement(String variableName, IExpression expression) {
        this.variableName = variableName;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState programState) throws ExpressionException, StatementException {
        MyIDictionary<String,Integer> symbolTable = programState.getSymbolTable();
        int address = symbolTable.get(this.variableName);
        int value = this.expression.evaluate(symbolTable,programState.getHeap());

        try {
            programState.getHeap().updateValue(address, value);
        }catch (HeapException e) {
            throw new StatementException(e.getMessage());
        }

        return null;
    }

    @Override
    public String toString() {
        return "WriteHeapStatement(" + this.variableName + "," + this.expression + ")";
    }
}
