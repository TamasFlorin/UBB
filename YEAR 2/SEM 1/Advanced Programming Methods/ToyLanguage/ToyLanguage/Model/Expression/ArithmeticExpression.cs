using ToyLanguage.Util.Dictionary;

namespace ToyLanguage.Model.Expression
{
    class ArithmeticExpression : IExpression
    {
        private readonly IExpression operand1;
        private readonly IExpression operand2;
        private readonly char operatorSymbol;

        public ArithmeticExpression(char operatorSymbol,IExpression operand1,IExpression operand2)
        {
            this.operatorSymbol = operatorSymbol;
            this.operand1 = operand1;
            this.operand2 = operand2;
        }

        public int Evaluate(MyIDictionary<string, int> symbolTable)
        {
            int first = operand1.Evaluate(symbolTable);
            int second = operand2.Evaluate(symbolTable);

            switch (operatorSymbol)
            {
                case '+': return first + second;
                case '-': return first - second;
                case '*': return first * second;
                case '/':
                if (second == 0)
                    throw new ExpressionException("Division by 0!");
                return first / second;
                default:
                    throw new ExpressionException("Invalid operator!");
            }
        }

        public override string ToString()
        {
            return "ArithmeticExpression(" + operand1 + " " + operatorSymbol + " " + operand2 + ")";
        }
    }
}
