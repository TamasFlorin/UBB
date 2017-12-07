package Repository;

import Model.State.ProgramState;
import Model.Statement.IStatement;
import Util.Dictionary.MyIDictionary;
import Util.List.MyIList;
import Util.Stack.MyIStack;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class MemoryRepository implements IRepository {
    private List<ProgramState> list;
    private String logFilePath;

    public MemoryRepository() {
        this.logFilePath = null;
        this.list = new ArrayList<>();
    }

    public MemoryRepository(String logFilePath) {
        this.logFilePath = logFilePath;
        this.list = new ArrayList<>();
    }

    private void logState(ProgramState state,PrintWriter logWriter) {
        MyIStack<IStatement> executionStack = state.getExecutionStack();
        MyIDictionary<String,Integer> symbolTable = state.getSymbolTable();
        MyIList<Integer> output = state.getOutput();

        logWriter.println("STACK:");
        logWriter.println(executionStack);
        logWriter.println("SYMBOL TABLE:");
        logWriter.println(symbolTable);
        logWriter.println("OUTPUT:");
        logWriter.println(output);
        logWriter.println("FILE TABLE:");
        logWriter.println(state.getFileTable());
        logWriter.println("HEAP:");
        logWriter.println(state.getHeap());
    }

    @Override
    public void add(ProgramState element) {
        this.list.add(element);
    }

    @Override
    public ProgramState back() throws RepositoryException {
        if(this.list.size() == 0)
            throw new RepositoryException("Empty repository!");

        return this.list.get(this.list.size() - 1);
    }

    @Override
    public void logData() throws RepositoryException {
        PrintWriter logWriter;

        try {
            logWriter = new PrintWriter(new BufferedWriter(new FileWriter(this.logFilePath, true)));
        }catch(IOException ex) {
            throw new RepositoryException("Could not open log file!");
        }

        for(ProgramState state : this.list) {
            logWriter.println("========== STATE ==========");
            this.logState(state,logWriter);
        }

        logWriter.println("---------------------------------");
        logWriter.close();
    }
}
