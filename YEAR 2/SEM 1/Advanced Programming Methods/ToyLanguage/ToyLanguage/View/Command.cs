using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ToyLanguage.View
{
    abstract class Command
    {
        private readonly string key;
        private readonly string description;

        public Command(string key,string description)
        {
            this.key = key;
            this.description = description;
        }

        public abstract void Execute();

        public string Key => key;
        public string Description => description;
    }
}
