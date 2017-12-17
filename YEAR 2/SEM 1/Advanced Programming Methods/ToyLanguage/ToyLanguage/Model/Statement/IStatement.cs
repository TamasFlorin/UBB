using ToyLanguage.Model.State;

namespace ToyLanguage.Model.Statement
{
    interface IStatement
    {
        ProgramState Execute(ProgramState programState);
    }
}
