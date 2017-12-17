using ToyLanguage.Util.Dictionary;

namespace ToyLanguage.Model.Expression
{
    class ConstantExpression : IExpression
    {
        private readonly int number;

        public ConstantExpression(int number)
        {
            this.number = number;
        }

        public int Evaluate(MyIDictionary<string, int> symbolTable)
        {
            return number;
        }

        public override string ToString()
        {
            return "ConstantExpression(" + number + ")";
        }
    }
}
