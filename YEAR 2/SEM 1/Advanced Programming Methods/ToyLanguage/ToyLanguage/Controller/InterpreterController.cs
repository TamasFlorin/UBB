using System;
using System.Diagnostics;
using ToyLanguage.Model.State;
using ToyLanguage.Model.Statement;
using ToyLanguage.Repository;
using ToyLanguage.Util.Stack;

namespace ToyLanguage.Controller
{
    class InterpreterController
    {
        private readonly IRepository repository;
        public InterpreterController(IRepository repository)
        {
            this.repository = repository;
        }

        private ProgramState ExecuteOneStep(ProgramState programState)
        {
            MyIStack<IStatement> executionStack = programState.ExecutionStack;

            if (executionStack.IsEmpty) throw new InterpreterControllerException("Execution stack is empty!");

            IStatement current = executionStack.Pop();

            return current.Execute(programState);
        }

        public void ExecuteAllSteps()
        {
            // nothing to execute
            if (repository.IsEmpty) return;

            ProgramState programState = repository.Get(0);
            MyIStack<IStatement> executionStack = programState.ExecutionStack;

            while (!executionStack.IsEmpty)
            {
                ExecuteOneStep(programState);
                repository.LogData();
            }
        }
    }
}
