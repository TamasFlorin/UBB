package Model.Statement;

import Model.Expression.ExpressionException;
import Model.State.ProgramState;
import Util.Dictionary.MyDictionary;
import Util.Dictionary.MyIDictionary;
import Util.Stack.MyIStack;
import Util.Stack.MyStack;

public class ForkStatement implements IStatement {
    private IStatement statement;

    public ForkStatement(IStatement statement){ this.statement = statement; }

    @Override
    public ProgramState execute(ProgramState programState) throws ExpressionException, StatementException {

        MyIStack<IStatement> stack = new MyStack<>();
        stack.push(this.statement);
        MyIDictionary<String,Integer> symbolTable = new MyDictionary<>(programState.getSymbolTable());
        long newId = programState.getId() * 10;

        return new ProgramState(stack,symbolTable,programState.getOutput(),
                programState.getFileTable(),programState.getHeap(),newId);
    }

    @Override
    public String toString() {
        return "Fork(" + this.statement + ")";
    }
}
