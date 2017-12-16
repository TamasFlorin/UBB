package Model.State;

import Model.Statement.IStatement;
import Model.Statement.StatementException;
import Util.Dictionary.MyIDictionary;
import Util.Heap.IHeap;
import Util.List.MyIList;
import Util.Stack.MyIStack;
import Util.Tuple.Tuple;

import java.io.BufferedReader;

public class ProgramState {
    private MyIStack<IStatement> executionStack;
    private MyIDictionary<String,Integer> symbolTable;
    private MyIList<Integer> output;
    private MyIDictionary<Integer,Tuple<String,BufferedReader>> fileTable;
    private IHeap heap;
    private long id;

    public ProgramState(MyIStack<IStatement> executionStack, MyIDictionary<String, Integer> symbolTable,
                        MyIList<Integer> output, MyIDictionary<Integer, Tuple<String, BufferedReader>> fileTable, IHeap heap,long id) {

        this.executionStack = executionStack;
        this.symbolTable = symbolTable;
        this.output = output;
        this.fileTable = fileTable;
        this.heap = heap;
        this.id = id;
    }

    public MyIStack<IStatement> getExecutionStack() {
        return this.executionStack;
    }

    public MyIDictionary<String,Integer> getSymbolTable() {
        return this.symbolTable;
    }

    public MyIList<Integer> getOutput() {return this.output;}

    public MyIDictionary<Integer,Tuple<String,BufferedReader>> getFileTable() {
        return this.fileTable;
    }

    public IHeap getHeap() {
        return this.heap;
    }

    public boolean isCompleted() { return this.executionStack.isEmpty(); }

    public long getId()
    {
        return this.id;
    }

    public ProgramState oneStep() throws StatementException {
        if(this.getExecutionStack().isEmpty()) throw new StatementException("Empty stack!");
        try {
            IStatement current = this.getExecutionStack().pop();
            return current.execute(this);
        }catch(Exception ex)
        {
            throw new StatementException("Could not execute current statement!");
        }
    }
    
    @Override
    public String toString() {
        return "state ID: " + id + "\n" + "Stack:\n" + executionStack + "Symbol table:\n" + symbolTable + "Output:\n" + output + "\n";
    }
}
