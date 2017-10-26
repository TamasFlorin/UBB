package Model.Statement;

import Model.Expression.ExpressionException;
import Model.Expression.IExpression;
import Model.State.ProgramState;
import Util.Dictionary.MyIDictionary;
import Util.Tuple.Tuple;

import java.io.BufferedReader;
import java.io.IOException;

public class CloseFileStatement implements IStatement {
    private IExpression expFileId;

    public CloseFileStatement(IExpression expFileId) {
        this.expFileId = expFileId;
    }

    @Override
    public ProgramState execute(ProgramState programState) throws ExpressionException, StatementException {
        MyIDictionary<String,Integer> symbolTable = programState.getSymbolTable();
        int fileId = expFileId.evaluate(symbolTable);

        Tuple<String, BufferedReader> tuple = programState.getFileTable().get(fileId);

        if( tuple == null) {
            throw new StatementException("No entry in the file table for the given value!");
        }

        // close BufferedReader
        BufferedReader bufferedReader = tuple.getSecond();

        try {
            bufferedReader.close();
        }catch(IOException ex){
            throw new StatementException("Could not close file!");
        }

        // delete entry
        programState.getFileTable().remove(fileId);

        return programState;
    }
}
