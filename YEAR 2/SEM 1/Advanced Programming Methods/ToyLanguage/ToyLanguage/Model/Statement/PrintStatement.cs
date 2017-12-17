using ToyLanguage.Model.Expression;
using ToyLanguage.Model.State;

namespace ToyLanguage.Model.Statement
{
    class PrintStatement : IStatement
    {
        private readonly IExpression expression;

        public PrintStatement(IExpression expression)
        {
            this.expression = expression;
        }

        public ProgramState Execute(ProgramState programState)
        {
            int value = expression.Evaluate(programState.SymbolTable);
            programState.Output.Add(value);

            return programState;
        }

        public override string ToString()
        {
            return "PrintStatement(" + expression + ")";
        }
    }
}
