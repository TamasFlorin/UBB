using System;
using System.IO;
using ToyLanguage.Model.Expression;
using ToyLanguage.Model.State;
using ToyLanguage.Util.Dictionary;

namespace ToyLanguage.Model.Statement
{
    class ReadFileStatement : IStatement
    {
        private readonly string varName;
        private readonly IExpression expFileId;
        public ReadFileStatement(IExpression expFileId,string varName)
        {
            this.expFileId = expFileId;
            this.varName = varName;
        }

        public ProgramState Execute(ProgramState programState)
        {
            MyIDictionary<string, int> symbolTable = programState.SymbolTable;

            int fileDescriptor = expFileId.Evaluate(symbolTable);

            if(!programState.FileTable.TryGetValue(fileDescriptor, out Tuple<string, TextReader> value))
            {
                throw new StatementException("Invalid file id provided!");
            }

            TextReader reader = value.Item2;
            string line;

            try
            {
                line = reader.ReadLine();
            }catch(Exception)
            {
                throw new StatementException("Error while reading from file!");
            }

            int intValue = 0;

            if (line != null && !int.TryParse(line, out intValue))
            {
                throw new StatementException("File contains non-numeric values!");
            }

            if (symbolTable.ContainsKey(varName))
                symbolTable.Update(varName, intValue);
            else
                symbolTable.Add(varName, intValue);

            return programState;
        }

        public override string ToString()
        {
            return "ReadFileStatement(" + expFileId + "," + varName + ")";
        }
    }
}
