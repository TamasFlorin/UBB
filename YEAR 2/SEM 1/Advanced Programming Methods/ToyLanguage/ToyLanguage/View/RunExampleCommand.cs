using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ToyLanguage.Controller;

namespace ToyLanguage.View
{
    class RunExampleCommand : Command
    {
        private readonly InterpreterController controller;
        public RunExampleCommand(string key, string description,InterpreterController controller) : base(key, description)
        {
            this.controller = controller;
        }

        public override void Execute()
        {
            try
            {
                controller.ExecuteAllSteps();
            }
            catch (Exception ex)
            {
                Console.WriteLine("An error ocurred: " + ex);
            }
        }
    }
}
