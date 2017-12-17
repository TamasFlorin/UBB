using ToyLanguage.Model.State;

namespace ToyLanguage.Repository
{
    interface IRepository
    {
        void Add(ProgramState programState);
        ProgramState Get(int index);

        bool IsEmpty
        {
            get;
        }

        void LogData();
    }
}
