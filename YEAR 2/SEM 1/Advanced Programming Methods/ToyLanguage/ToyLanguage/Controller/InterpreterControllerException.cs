using System;

namespace ToyLanguage.Controller
{
    class InterpreterControllerException : Exception
    {
        public InterpreterControllerException(string message) : base(message)
        {

        }
    }
}
