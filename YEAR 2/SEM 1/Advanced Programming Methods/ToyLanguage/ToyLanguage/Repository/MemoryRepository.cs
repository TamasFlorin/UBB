using System;
using ToyLanguage.Model.State;
using ToyLanguage.Util.List;
using System.IO;

namespace ToyLanguage.Repository
{
    class MemoryRepository : IRepository
    {
        private readonly MyIList<ProgramState> data = new MyList<ProgramState>();
        private readonly string logFile;

        public MemoryRepository(string logFile)
        {
            if (File.Exists(logFile))
                File.Delete(logFile);

            this.logFile = logFile;
        }

        public bool IsEmpty => data.Count == 0;

        public void Add(ProgramState programState)
        {
            data.Add(programState);
        }

        public ProgramState Get(int index)
        {
            if (index < 0 || index > data.Count) throw new MemoryRepositoryException("Invalid index!");

            return data.ElementAt(index);
        }
        
        private void LogProgramState(ProgramState programState,StreamWriter writer)
        {
            writer.WriteLine("==== Program State ====");
            writer.WriteLine("ExecutionStack:");
            writer.WriteLine(programState.ExecutionStack);
            writer.WriteLine("SymbolTable:");
            writer.WriteLine(programState.SymbolTable);
            writer.WriteLine("Output:");
            writer.WriteLine(programState.Output);
            writer.WriteLine("File table:");
            writer.WriteLine(programState.FileTable);
        }

        public void LogData()
        {
            try
            { 
                StreamWriter writer = new StreamWriter(logFile, true);
            
                for(int i = 0; i < data.Count; i++)
                {
                    LogProgramState(data.ElementAt(0),writer);
                }
                
                writer.Close();
            }catch(Exception)
            {
                throw new MemoryRepositoryException("Could not write data to log file!");
            }
        }
    }
}
