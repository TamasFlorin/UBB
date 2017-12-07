package Model.State;

import Model.Statement.IStatement;
import Util.Dictionary.MyIDictionary;
import Util.Heap.IHeap;
import Util.List.MyIList;
import Util.Stack.MyIStack;
import Util.Tuple.Tuple;

import java.io.BufferedReader;

public class ProgramState {
    private IStatement program; // will be used later
    private MyIStack<IStatement> executionStack;
    private MyIDictionary<String,Integer> symbolTable;
    private MyIList<Integer> output;
    private MyIDictionary<Integer,Tuple<String,BufferedReader>> fileTable;
    private IHeap heap;

    public ProgramState(MyIStack<IStatement> executionStack, MyIDictionary<String, Integer> symbolTable,
                        MyIList<Integer> output, IStatement program, MyIDictionary<Integer, Tuple<String, BufferedReader>> fileTable, IHeap heap) {

        this.executionStack = executionStack;
        this.symbolTable = symbolTable;
        this.program = program;
        this.output = output;
        this.fileTable = fileTable;
        this.heap = heap;
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
    
    @Override
    public String toString() {
        return "Stack:\n" + executionStack + "Symbol table:\n" + symbolTable + "Output:\n" + output + "\n";
    }
}
