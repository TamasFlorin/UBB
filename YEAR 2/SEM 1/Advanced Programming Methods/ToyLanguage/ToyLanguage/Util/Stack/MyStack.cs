using System.Collections.Generic;
using System.Text;

namespace ToyLanguage.Util.Stack
{
    class MyStack<T> : MyIStack<T>
    {
        private readonly Stack<T> stack = new Stack<T>();

        public bool IsEmpty => stack.Count == 0;

        public T Pop()
        {
            if (IsEmpty) throw new MyStackException("Pop from empty stack!");

            return stack.Pop();
        }

        public void Push(T item)
        {
            stack.Push(item);
        }

        public T Peek()
        {
            if (IsEmpty) throw new MyStackException("Top on empty stack!");

            return stack.Peek();
        }

        public override string ToString()
        {
            StringBuilder builder = new StringBuilder();
            var items = stack.ToArray();

            for(int i = 0; i < items.Length;i++)
            {
                builder.Append(items[i]);
                builder.Append(System.Environment.NewLine);
            }

            return builder.ToString();
        }
    }
}
