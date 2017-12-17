using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ToyLanguage.Model.State;
using ToyLanguage.Util.Table;

namespace ToyLanguage.Model.Statement
{
    class OpenFileStatement : IStatement
    {
        private string varFileId;
        private string fileName;

        public OpenFileStatement(string varFileId,string fileName)
        {
            this.varFileId = varFileId;
            this.fileName = fileName;
        }
        public ProgramState Execute(ProgramState programState)
        {
            FileTable fileTable = programState.FileTable;

            if (fileTable.FileExists(fileName)) throw new StatementException("Duplicate file name!");

            int fileDescriptor;

            try
            {
                fileDescriptor = fileTable.Add(fileName);
            }catch(FileTableException ex)
            {
                throw new StatementException("Could not add file to FileTable: " + ex.ToString());
            }

            if(programState.SymbolTable.ContainsKey(varFileId))
                programState.SymbolTable.Update(varFileId, fileDescriptor);
            else
                programState.SymbolTable.Add(varFileId, fileDescriptor);

            return programState;
        }
    }
}
