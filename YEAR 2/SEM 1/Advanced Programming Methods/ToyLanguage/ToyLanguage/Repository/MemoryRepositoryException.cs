using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ToyLanguage.Repository
{
    class MemoryRepositoryException : Exception
    {
        public MemoryRepositoryException(string message) : base(message)
        {

        }
    }
}
