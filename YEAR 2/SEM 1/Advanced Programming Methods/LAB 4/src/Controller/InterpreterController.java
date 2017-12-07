package Controller;

import Model.Expression.ExpressionException;
import Model.Statement.IStatement;
import Model.State.ProgramState;
import Model.Statement.StatementException;
import Repository.IRepository;
import Repository.RepositoryException;
import Util.Heap.HeapException;
import Util.Stack.MyIStack;
import Util.Stack.StackException;

import java.io.IOException;
import java.util.Collection;
import java.util.Map;
import java.util.stream.Collectors;

public class InterpreterController {
    private IRepository repository;

    public InterpreterController(IRepository repository) {
        this.repository = repository;
    }

    private void conservativeGarbageCollector() throws HeapException, RepositoryException {
        ProgramState programState = this.repository.back();

        programState.getHeap().garbageCollect(programState.getSymbolTable().values());
    }

    private void closeFiles() throws RepositoryException
    {
        // TODO: finish implementing this
        ProgramState programState = this.repository.back();
    }

    private ProgramState executeOneStep(ProgramState state) throws ExpressionException, StackException, RepositoryException, StatementException {
        ProgramState programState = this.repository.back();
        MyIStack<IStatement> stack = programState.getExecutionStack();
        IStatement statement = stack.pop();

        return statement.execute(state);
    }

    public void executeAllSteps() throws ExpressionException, StackException, RepositoryException, StatementException, HeapException {
        try {
            ProgramState programState = this.repository.back();

            while (!programState.getExecutionStack().isEmpty()) {
                this.executeOneStep(programState);
                this.conservativeGarbageCollector();
                this.repository.logData();
            }
        }catch(Exception ex) {
            ex.printStackTrace();
        }
        finally{
            this.closeFiles();
        }
    }
}
