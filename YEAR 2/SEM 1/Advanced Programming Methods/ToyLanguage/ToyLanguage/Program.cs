using System.Diagnostics;
using System.IO;
using ToyLanguage.Controller;
using ToyLanguage.Model.Expression;
using ToyLanguage.Model.State;
using ToyLanguage.Model.Statement;
using ToyLanguage.Repository;
using ToyLanguage.Util.Dictionary;
using ToyLanguage.Util.List;
using ToyLanguage.Util.Stack;
using ToyLanguage.View;

namespace ToyLanguage
{
    class Program
    {
        static IStatement MakeCompountStatement(params IStatement [] statements)
        {
            Debug.Assert(statements.Length > 0);

            IStatement statement = statements[0];

            for (int i = 1; i < statements.Length; i++)
            {
                IStatement current = statements[i];
                statement = new CompoundStatement(statement, current);
            }

            return statement;
        }

        static Command GetRunCommand(string key, string description,params IStatement[] statements)
        {
            IStatement statement = MakeCompountStatement(statements);

            MyIStack<IStatement> executionStack = new MyStack<IStatement>();
            executionStack.Push(statement);

            MyIDictionary<string, int> symbolTable = new MyDictionary<string, int>();
            MyIList<int> output = new MyList<int>();
            ProgramState programState = new ProgramState(executionStack, symbolTable, output);
            IRepository repository = new MemoryRepository("log.txt");
            repository.Add(programState);
            InterpreterController controller = new InterpreterController(repository);

            return new RunExampleCommand(key, description, controller);
        }

        static void Main(string[] args)
        {
            TextMenu textMenu = new TextMenu();

            textMenu.AddCommand(new ExitCommand("0", "Exit"));

            // first example: v=2;Print(v)
            Command ex1 = GetRunCommand("1",
                "Basic statements example",
                new AssignmentStatement("v", new ConstantExpression(2)),
                new PrintStatement(new VariableExpression("v")));

            Command ex2 = GetRunCommand(
                "2",
                "Example of working with files",
                new OpenFileStatement("var_f", "input.txt"),
                new ReadFileStatement(new VariableExpression("var_f"), "var_c"),
                new PrintStatement(new VariableExpression("var_c")),
                new IfStatement(new VariableExpression("var_c"),
                    new CompoundStatement(new ReadFileStatement(new VariableExpression("var_f"), "var_c"),
                            new PrintStatement(new VariableExpression("var_c"))),
                    new PrintStatement(new ConstantExpression(0))),
                    new CloseFileStatement(new VariableExpression("var_f"))
                );

            textMenu.AddCommand(ex1);
            textMenu.AddCommand(ex2);
            textMenu.Show();
        }
    }
}
