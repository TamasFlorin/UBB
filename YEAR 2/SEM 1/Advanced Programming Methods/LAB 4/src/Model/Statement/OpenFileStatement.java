package Model.Statement;

import Model.Expression.ExpressionException;
import Model.Expression.IExpression;
import Model.Expression.VariableExpression;
import Model.State.ProgramState;
import Util.Dictionary.MyIDictionary;
import Util.Tuple.Tuple;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;

public class OpenFileStatement implements IStatement {
    private String varFileId;
    private String fileName;

    public OpenFileStatement(String varFileId, String fileName){
        this.varFileId = varFileId;
        this.fileName = fileName;
    }

    @Override
    public ProgramState execute(ProgramState programState) throws ExpressionException, StatementException{
        MyIDictionary<Integer,Tuple<String,BufferedReader>> fileTable = programState.getFileTable();

        /*if(fileTable.containsValue(new Tuple<String,BufferedReader>(this.fileName,null))) {
            throw new StatementException("Duplicate file name!");
        }*/

        // check if file name is already in the file table
        for(Tuple<String,BufferedReader> tuple : fileTable.values()){
            if( tuple.getFirst().equals(this.fileName))
                throw new StatementException("There is already a file descriptor attached to that name!");
        }

        BufferedReader bufferedReader;

        try {
            bufferedReader = new BufferedReader(new FileReader(this.fileName));
        }catch(FileNotFoundException ex) {
            throw new StatementException("Could not open file!");
        }

        int uniqueId = bufferedReader.hashCode();

        fileTable.put(uniqueId,new Tuple<>(this.fileName,bufferedReader));

        MyIDictionary<String,Integer> symbolTable = programState.getSymbolTable();

        symbolTable.put(varFileId,uniqueId);

        return programState;
    }
}
