using ToyLanguage.Model.Expression;
using ToyLanguage.Model.State;
using ToyLanguage.Util.Dictionary;

namespace ToyLanguage.Model.Statement
{
    class AssignmentStatement : IStatement
    {
        private readonly string id;
        private readonly IExpression expression;

        public AssignmentStatement(string id,IExpression expression)
        {
            this.id = id;
            this.expression = expression;
        }

        public ProgramState Execute(ProgramState programState)
        {
            MyIDictionary<string, int> symbolTable = programState.SymbolTable;

            int value = expression.Evaluate(symbolTable);

            if(symbolTable.ContainsKey(id))
            {
                symbolTable.Update(id, value);
            }
            else
            {
                symbolTable.Add(id, value);
            }

            return programState;
        }

        public override string ToString()
        {
            return "AssignmentStatement(" + id + "," + expression + ")";
        }
    }
}
