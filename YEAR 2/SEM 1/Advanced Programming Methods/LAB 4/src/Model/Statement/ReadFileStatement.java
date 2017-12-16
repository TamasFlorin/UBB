package Model.Statement;

import Model.Expression.ExpressionException;
import Model.Expression.IExpression;
import Model.State.ProgramState;
import Util.Dictionary.MyIDictionary;
import Util.Tuple.Tuple;

import java.io.BufferedReader;
import java.io.IOException;

public class ReadFileStatement implements IStatement {
    private String varName;
    private IExpression expFileId;

    public ReadFileStatement(IExpression expFileId,String varName) {
        this.expFileId = expFileId;
        this.varName = varName;
    }
    @Override
    public ProgramState execute(ProgramState programState) throws ExpressionException, StatementException {
        MyIDictionary<String,Integer> symbolTable = programState.getSymbolTable();

        int uniqueId = expFileId.evaluate(symbolTable,programState.getHeap());
        Tuple<String, BufferedReader> tuple = programState.getFileTable().get(uniqueId);

        if( tuple == null){
            throw new StatementException("Could not open file!");
        }

        BufferedReader bufferedReader = tuple.getSecond();

        String line;
        try {
            line = bufferedReader.readLine();
        }catch(IOException ex) {
            throw new StatementException("An error occurred while reading the file!");
        }

        int value = (line == null) ? 0 : Integer.parseInt(line);

        symbolTable.put(this.varName,value);

        return null;
    }

    @Override
    public String toString() {
        return "ReadFileStatement(" + this.varName + "," + this.expFileId + ")";
    }
}
