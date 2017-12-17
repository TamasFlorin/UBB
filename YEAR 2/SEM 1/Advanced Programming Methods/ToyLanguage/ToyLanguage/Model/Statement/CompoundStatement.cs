using ToyLanguage.Model.State;
using ToyLanguage.Util.Stack;

namespace ToyLanguage.Model.Statement
{
    class CompoundStatement : IStatement
    {
        private readonly IStatement first;
        private readonly IStatement second;

        public CompoundStatement(IStatement first,IStatement second)
        {
            this.first = first;
            this.second = second;
        }

        public ProgramState Execute(ProgramState programState)
        {
            MyIStack<IStatement> executionStack = programState.ExecutionStack;

            executionStack.Push(second);
            executionStack.Push(first);

            return programState;
        }

        public override string ToString()
        {
            return "CompoundStatement(" + this.first + "," + this.second + ")";
        }
    }
}
