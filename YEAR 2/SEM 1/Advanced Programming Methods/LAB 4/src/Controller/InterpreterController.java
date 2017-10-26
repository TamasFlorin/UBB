package Controller;

import Model.Expression.ExpressionException;
import Model.Statement.IStatement;
import Model.State.ProgramState;
import Model.Statement.StatementException;
import Repository.IRepository;
import Repository.RepositoryException;
import Util.Stack.MyIStack;
import Util.Stack.StackException;

import java.io.IOException;

public class InterpreterController {
    private IRepository repository;

    public InterpreterController(IRepository repository) {
        this.repository = repository;
    }

    public ProgramState executeOneStep(ProgramState state) throws ExpressionException, StackException, RepositoryException, StatementException, IOException {
        ProgramState programState = this.repository.back();
        MyIStack<IStatement> stack = programState.getExecutionStack();
        IStatement statement = stack.pop();

        return statement.execute(state);
    }

    public void executeAllSteps() throws ExpressionException, StackException, RepositoryException, StatementException, IOException {
        ProgramState programState = this.repository.back();

        while(!programState.getExecutionStack().isEmpty()){
            executeOneStep(programState);
            repository.logData();
        }
    }
}
