using ToyLanguage.Util.Dictionary;

namespace ToyLanguage.Model.Expression
{
    interface IExpression
    {
        int Evaluate(MyIDictionary<string, int> symbolTable);
    }
}
