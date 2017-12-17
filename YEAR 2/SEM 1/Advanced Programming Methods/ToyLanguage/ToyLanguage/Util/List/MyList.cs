using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ToyLanguage.Util.List
{
    class MyList<T> : MyIList<T>
    {
        private readonly IList<T> list = new List<T>();

        public int Count => list.Count;

        public void Add(T item)
        {
            list.Add(item);
        }

        public T ElementAt(int index)
        {
            if (index < 0 || index >= list.Count) throw new MyListException("Invalid index!");

            return list.ElementAt(index);
        }

        public override string ToString()
        {
            StringBuilder builder = new StringBuilder();

            foreach(var item in list)
            {
                builder.Append(item);
                builder.Append(System.Environment.NewLine);
            }

            return builder.ToString();
        }
    }
}
