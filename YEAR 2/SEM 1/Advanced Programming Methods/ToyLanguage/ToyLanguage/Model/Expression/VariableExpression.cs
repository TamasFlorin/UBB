using ToyLanguage.Util.Dictionary;

namespace ToyLanguage.Model.Expression
{
    class VariableExpression : IExpression
    {
        private readonly string id;

        public VariableExpression(string id)
        {
            this.id = id;
        }

        public int Evaluate(MyIDictionary<string, int> symbolTable)
        {
            if (!symbolTable.TryGetValue(id, out int value)) throw new ExpressionException("Unassigned variable used!");

            return value;
        }

        public override string ToString()
        {
            return "VariableExpression(" + id + ")";
        }
    }
}
