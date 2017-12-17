using System.IO;
using ToyLanguage.Controller;
using ToyLanguage.Model.Expression;
using ToyLanguage.Model.State;
using ToyLanguage.Model.Statement;
using ToyLanguage.Repository;
using ToyLanguage.Util.Dictionary;
using ToyLanguage.Util.List;
using ToyLanguage.Util.Stack;

namespace ToyLanguage
{
    class Program
    {
        static void Main(string[] args)
        {
            MyIStack<IStatement> executionStack = new MyStack<IStatement>();

            // example: v=2;Print(v)
            IStatement firstExample = 
                new CompoundStatement(
                new PrintStatement(new VariableExpression("v")),
                new AssignmentStatement("v", new ConstantExpression(2)));

            //executionStack.Push(firstExample);
            IStatement openFile = new OpenFileStatement("var_f", "input.txt");
            IStatement readFile = new ReadFileStatement(new VariableExpression("var_f"), "var_c");
            IStatement printC = new PrintStatement(new VariableExpression("var_c"));

            IStatement check = new IfStatement(new VariableExpression("var_c"),
                    new CompoundStatement(new ReadFileStatement(new VariableExpression("var_f"), "var_c"),
                            new PrintStatement(new VariableExpression("var_c"))),
                    new PrintStatement(new ConstantExpression(0)));

            IStatement closeFile = new CloseFileStatement(new VariableExpression("var_f"));
            IStatement openFile2 = new OpenFileStatement("var_f1", "input1.txt");
            IStatement openFile3 = new OpenFileStatement("var_f2", "input2.txt");
            IStatement openFile4 = new OpenFileStatement("var_f3", "input3.txt");

            executionStack.Push(openFile);
            executionStack.Push(openFile4);
            executionStack.Push(openFile3);
            executionStack.Push(openFile2);
            executionStack.Push(closeFile);
            executionStack.Push(check);
            executionStack.Push(printC);
            executionStack.Push(readFile);
            executionStack.Push(openFile);

            MyIDictionary<string, int> symbolTable = new MyDictionary<string, int>();
            MyIList<int> output = new MyList<int>();
            ProgramState programState = new ProgramState(executionStack, symbolTable, output);
            IRepository repository = new MemoryRepository("log.txt");
            repository.Add(programState);
            InterpreterController controller = new InterpreterController(repository);
            controller.ExecuteAllSteps();
        }
    }
}
