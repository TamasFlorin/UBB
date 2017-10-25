import Controller.InterpreterController;
import Model.Expression.ArithmeticExpression;
import Model.Expression.ConstantExpression;
import Model.Expression.VariableExpression;
import Model.State.ProgramState;
import Model.Statement.*;
import Repository.IRepository;
import Repository.MemoryRepository;
import Util.Dictionary.MyDictionary;
import Util.Dictionary.MyIDictionary;
import Util.List.MyIList;
import Util.List.MyList;
import Util.Stack.MyIStack;
import Util.Stack.MyStack;

public class Main {
    public static void main(String[] args) {
        IStatement first =  new AssignmentStatement("a",new ConstantExpression(2));
        IStatement second = new AssignmentStatement("b",
                            new ArithmeticExpression('+',
                            new VariableExpression("a"),
                            new ConstantExpression(10))
        );

        IStatement third = new IfStatement(new ConstantExpression(1),
                           new PrintStatement(new VariableExpression("a")),
                           new PrintStatement(new VariableExpression("b"))
        );

        IStatement fourth = new CompoundStatement(
                           new PrintStatement(
                           new VariableExpression("a")),
                           new PrintStatement(
                           new VariableExpression("b"))
        );

        MyIStack<IStatement> executionStack = new MyStack<>();

        executionStack.push(fourth);
        executionStack.push(third);
        executionStack.push(second);
        executionStack.push(first);

        MyIDictionary<String, Integer> symbolTable= new MyDictionary<>() {};
        MyIList<Integer> output = new MyList<>();
        ProgramState state = new ProgramState(executionStack,symbolTable,output,first);

        IRepository<ProgramState> repository = new MemoryRepository<>();
        repository.add(state);
        InterpreterController controller = new InterpreterController(repository);

        try {
            controller.executeAllSteps();
        }
        catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
}
