using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ToyLanguage.Util.Dictionary;

namespace ToyLanguage.View
{
    class TextMenu
    {
        private readonly MyIDictionary<string, Command> commands = new MyDictionary<string, Command>();

        public TextMenu() { }

        public void AddCommand(Command command)
        {
            commands.Add(command.Key, command);
        }

        private void PrintMenu()
        {
            foreach(var command in commands)
            {
                string line = string.Format("{0}: {1}", command.Key, command.Value.Description);
                Console.WriteLine(line);
            }
        }

        public void Show()
        {
            while(true)
            {
                PrintMenu();
                Console.WriteLine("Input command:");
                string key = Console.ReadLine();

                if (!commands.TryGetValue(key, out Command command))
                {
                    Console.WriteLine("Invalid command provided!");
                }
                else
                {
                    command.Execute();
                }
            }
        }
    }
}
