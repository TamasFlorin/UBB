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
import Util.Tuple.Tuple;
import View.ExitCommand;
import View.RunExampleCommand;
import View.TextView;

import java.io.BufferedReader;

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

        IStatement openFile = new OpenFileStatement("var_f","1.txt");
        IStatement readFile = new ReadFileStatement(new VariableExpression("var_f"),"var_c");
        IStatement printC = new PrintStatement(new VariableExpression("var_c"));

        IStatement check = new IfStatement(new VariableExpression("var_c"),
                new CompoundStatement(new ReadFileStatement(new VariableExpression("var_f"),"var_c"),
                        new PrintStatement(new VariableExpression("var_c"))),
                new PrintStatement(new ConstantExpression(0)));

        IStatement closeFile = new CloseFileStatement(new VariableExpression("var_f"));

        MyIStack<IStatement> executionStack = new MyStack<>();

        executionStack.push(check);
        executionStack.push(printC);
        executionStack.push(readFile);
        executionStack.push(openFile);

        executionStack.push(fourth);
        executionStack.push(third);
        executionStack.push(second);
        executionStack.push(first);

        MyIDictionary<String, Integer> symbolTable= new MyDictionary<>();
        MyIDictionary<Integer,Tuple<String,BufferedReader>> fileTable = new MyDictionary<>();

        MyIList<Integer> output = new MyList<>();
        ProgramState state = new ProgramState(executionStack,symbolTable,output,first,fileTable);
        IRepository repository;
        InterpreterController controller;

        try {
            repository = new MemoryRepository("test.txt");
            repository.add(state);
            controller = new InterpreterController(repository);
            TextView view = new TextView();
            view.addCommand(new ExitCommand("0","exit"));
            view.addCommand(new RunExampleCommand("1","First example",controller));
            view.show();
        }
        catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
