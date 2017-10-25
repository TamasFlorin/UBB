package Controller;

import Model.Expression.ExpressionException;
import Model.Statement.IStatement;
import Model.State.ProgramState;
import Repository.IRepository;
import Repository.RepositoryException;
import Util.Stack.MyIStack;
import Util.Stack.StackException;

public class InterpreterController {
    private IRepository<ProgramState> repository;

    public InterpreterController(IRepository<ProgramState> repository) {
        this.repository = repository;
    }

    public ProgramState executeOneStep(ProgramState state) throws ExpressionException, StackException, RepositoryException {
        ProgramState programState = this.repository.back();
        MyIStack<IStatement> stack = programState.getExecutionStack();
        IStatement statement = stack.pop();

        return statement.execute(state);
    }

    public void executeAllSteps() throws ExpressionException, StackException, RepositoryException {
        ProgramState programState = this.repository.back();

        while(!programState.getExecutionStack().isEmpty()){
            executeOneStep(programState);
        }
    }
}
