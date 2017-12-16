import Controller.InterpreterController;
import Model.Expression.ArithmeticExpression;
import Model.Expression.ConstantExpression;
import Model.Expression.ReadHeapExpression;
import Model.Expression.VariableExpression;
import Model.State.ProgramState;
import Model.Statement.*;
import Repository.IRepository;
import Repository.MemoryRepository;
import Util.Dictionary.MyDictionary;
import Util.Dictionary.MyIDictionary;
import Util.Heap.Heap;
import Util.Heap.IHeap;
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

        // test heap allocation
        IStatement newVar = new AssignmentStatement("v",new ConstantExpression(10));
        IStatement newStatement = new NewStatement("v",new ConstantExpression(20));
        IStatement newStatement1 = new NewStatement("var_a",new ConstantExpression(22));
        IStatement writeHeap = new WriteHeapStatement("var_a",new ConstantExpression(30));
        IStatement printVar = new PrintStatement(new VariableExpression("var_a"));
        IStatement printHeapValue = new PrintStatement(new ReadHeapExpression("var_a"));
        IStatement assignStatement = new AssignmentStatement("var_a",new ConstantExpression(0));

        IStatement setV = new AssignmentStatement("v",new ConstantExpression(6));

        IStatement comp = new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                new AssignmentStatement("v",new ArithmeticExpression('-',new VariableExpression("v"),
                        new ConstantExpression(1))));

        IStatement whileStmt = new WhileStatement(new ArithmeticExpression('-',
                new VariableExpression("v"),new ConstantExpression(4)),comp);

        IStatement forkS = new CompoundStatement(
                new PrintStatement(
                        new ConstantExpression(4)
                ),
                new ForkStatement(
                        new PrintStatement( new ConstantExpression(2))
                )

        );

        MyIStack<IStatement> executionStack = new MyStack<>();

        /*
            Fork example
            v=10;new(a,22);
            fork(wH(a,30);v=32;print(v);print(rH(a)));
            print(v);print(rH(a))
        */

        executionStack.push(new PrintStatement(new VariableExpression("v")));
        executionStack.push(new PrintStatement(new ReadHeapExpression("a")));

        executionStack.push(new ForkStatement(new CompoundStatement(
                new WriteHeapStatement("a",new ConstantExpression(30)),
                new CompoundStatement(new AssignmentStatement("v",new ConstantExpression(32)),
                        new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                new PrintStatement(new ReadHeapExpression("a")))
                )


        )));
        executionStack.push(new NewStatement("a",new ConstantExpression(22)));
        executionStack.push(new AssignmentStatement("v",new ConstantExpression(10)));

        //executionStack.push(forkS);

        //executionStack.push(        new ForkStatement(
          //     new PrintStatement( new ConstantExpression(2))
        //));

        //executionStack.push(comp);
        //executionStack.push(whileStmt);
        //executionStack.push(setV);

        //executionStack.push(assignStatement);
        //executionStack.push(printHeapValue);
        //executionStack.push(printVar);
        //executionStack.push(writeHeap);
        //executionStack.push(newStatement1);
        //executionStack.push(newStatement);
        //executionStack.push(newVar);


        /*executionStack.push(check);
        executionStack.push(printC);
        executionStack.push(readFile);
        executionStack.push(openFile);

        executionStack.push(fourth);
        executionStack.push(third);
        executionStack.push(second);
        executionStack.push(first);
        */
        MyIDictionary<String, Integer> symbolTable = new MyDictionary<>();
        MyIDictionary<Integer,Tuple<String,BufferedReader>> fileTable = new MyDictionary<>();

        MyIList<Integer> output = new MyList<>();
        IHeap heap = new Heap();

        ProgramState state = new ProgramState(executionStack,symbolTable,output,fileTable, heap,1);
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
