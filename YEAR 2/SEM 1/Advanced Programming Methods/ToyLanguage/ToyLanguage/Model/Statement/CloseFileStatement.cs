using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ToyLanguage.Model.Expression;
using ToyLanguage.Model.State;
using ToyLanguage.Util.Dictionary;

namespace ToyLanguage.Model.Statement
{
    class CloseFileStatement : IStatement
    {
        private readonly IExpression expFileId;

        public CloseFileStatement(IExpression expFileId)
        {
            this.expFileId = expFileId;
        }
        public ProgramState Execute(ProgramState programState)
        {
            MyIDictionary<string, int> symbolTable = programState.SymbolTable;

            int fileDescriptor = expFileId.Evaluate(symbolTable);

            if (!programState.FileTable.TryGetValue(fileDescriptor, out Tuple<string, TextReader> value))
            {
                throw new StatementException("Invalid file id provided!");
            }

            TextReader reader = value.Item2;

            try
            {
                reader.Close();
            }
            catch (Exception)
            {
                throw new StatementException("Error while closing file!");
            }

            programState.FileTable.Remove(fileDescriptor);

            return programState;
        }
    }
}
