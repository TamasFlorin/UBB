using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ToyLanguage.Model.Statement
{
    class StatementException : Exception
    {
        public StatementException(string message) : base(message) { }
    }
}
