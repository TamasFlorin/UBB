using System;
using System.IO;
using ToyLanguage.Util.Dictionary;

namespace ToyLanguage.Util.Table
{
    class FileTable
    {
        private readonly MyIDictionary<int, Tuple<string, TextReader>> fileTable = 
            new MyDictionary<int, Tuple<string, TextReader>>();

        private readonly PositionTable positionTable = new PositionTable();

        public FileTable()
        {
        }

        public bool FileExists(string fileName)
        {
            foreach (var file in fileTable)
            {
                if (file.Value.Item1 == fileName)
                    return true;
            }

            return false;
        }

        public int Add(string fileName)
        {
            if (FileExists(fileName)) throw new FileTableException("Duplicate file name!");

            int fileDescriptor = positionTable.CurrentFree;

            TextReader reader;

            try
            {
                reader = new StreamReader(fileName);
            }catch(Exception)
            {
                throw new FileTableException("Could not open file!");
            }

            fileTable.Add(fileDescriptor, new Tuple<string, TextReader>(fileName,reader));

            positionTable.UpdateCurrentFree();

            return fileDescriptor;
        }

        public void Remove(int fileDescriptor)
        {
            if (!fileTable.TryGetValue(fileDescriptor, out Tuple<string, TextReader> value))
                throw new FileTableException("File is not in the file table!");

            value.Item2.Close();

            fileTable.Remove(fileDescriptor);

            positionTable.FreePosition(fileDescriptor);
        }

        public bool TryGetValue(int fileDescriptor,out Tuple<string, TextReader> file)
        {
            return fileTable.TryGetValue(fileDescriptor, out file);
        }

        public override string ToString()
        {
            return fileTable.ToString();
        }
    }
}
