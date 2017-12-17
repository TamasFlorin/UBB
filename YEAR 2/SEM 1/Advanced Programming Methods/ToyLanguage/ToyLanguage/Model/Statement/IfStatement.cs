using ToyLanguage.Model.Expression;
using ToyLanguage.Model.State;

namespace ToyLanguage.Model.Statement
{
    class IfStatement : IStatement
    {
        private readonly IExpression condition;
        private readonly IStatement thenStatement;
        private readonly IStatement elseStatement;

        public IfStatement(IExpression condition, IStatement thenStatement, IStatement elseStatement)
        {
            this.condition = condition;
            this.thenStatement = thenStatement;
            this.elseStatement = elseStatement;
        }

        public ProgramState Execute(ProgramState programState)
        {
            int value = condition.Evaluate(programState.SymbolTable);

            if( value != 0)
            {
                programState.ExecutionStack.Push(thenStatement);
            }
            else
            {
                programState.ExecutionStack.Push(elseStatement);
            }

            return programState;
        }

        public override string ToString()
        {
            return "IfStatement(" + condition + ")" + "Then " + thenStatement + " Else " + elseStatement;
        }
    }
}
