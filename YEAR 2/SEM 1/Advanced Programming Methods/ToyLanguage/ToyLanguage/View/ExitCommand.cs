﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ToyLanguage.View
{
    class ExitCommand : Command
    {
        public ExitCommand(string key, string description) : base(key, description)
        {
        }

        public override void Execute()
        {
            Environment.Exit(0);
        }
    }
}
