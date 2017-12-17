using ToyLanguage.Model.Statement;
using ToyLanguage.Util.Dictionary;
using ToyLanguage.Util.List;
using ToyLanguage.Util.Stack;
using ToyLanguage.Util.Table;

namespace ToyLanguage.Model.State
{
    class ProgramState
    {
        private readonly MyIStack<IStatement> executionStack;
        private readonly MyIDictionary<string, int> symbolTable;
        private readonly MyIList<int> output;
        private readonly FileTable fileTable = new FileTable();
        
        public ProgramState(MyIStack<IStatement> executionStack, MyIDictionary<string, int> symbolTable,
            MyIList<int> output)
        {
            this.executionStack = executionStack;
            this.symbolTable = symbolTable;
            this.output = output;
        }

        public MyIStack<IStatement> ExecutionStack => executionStack;

        public MyIDictionary<string, int> SymbolTable => symbolTable;

        public MyIList<int> Output => output;

        public FileTable FileTable => fileTable;
    }
}
