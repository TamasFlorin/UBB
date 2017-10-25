package Model.State;

import Model.Statement.IStatement;
import Util.Dictionary.MyIDictionary;
import Util.List.MyIList;
import Util.Stack.MyIStack;

public class ProgramState {
    private IStatement program; // will be used later
    private MyIStack<IStatement> executionStack;
    private MyIDictionary<String,Integer> symbolTable;
    private MyIList<Integer> output;

    public ProgramState(MyIStack<IStatement> executionStack, MyIDictionary<String,Integer> symbolTable,
                        MyIList<Integer> output,IStatement program) {

        this.executionStack = executionStack;
        this.symbolTable = symbolTable;
        this.program = program;
        this.output = output;
    }

    public MyIStack<IStatement> getExecutionStack() {
        return this.executionStack;
    }

    public MyIDictionary<String,Integer> getSymbolTable() {
        return this.symbolTable;
    }

    public MyIList<Integer> getOutput() {return this.output;}
}
