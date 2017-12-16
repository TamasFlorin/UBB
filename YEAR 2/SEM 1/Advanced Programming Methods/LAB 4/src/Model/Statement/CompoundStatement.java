package Model.Statement;

import Model.State.ProgramState;
import Util.Stack.MyIStack;

public class CompoundStatement implements IStatement {
    private IStatement first;
    private IStatement second;

    public CompoundStatement(IStatement first, IStatement second){
        this.first = first;
        this.second = second;
    }

    @Override
    public ProgramState execute(ProgramState programState) {
        MyIStack<IStatement> executionStack = programState.getExecutionStack();
        executionStack.push(this.second);
        executionStack.push(this.first);
        return null;
    }

    @Override
    public String toString() {
        return "(" + this.first + ";" + this.second + ")";
    }
}
