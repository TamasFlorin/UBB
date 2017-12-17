using System.Collections.Generic;
using System.Text;


namespace ToyLanguage.Util.Dictionary
{
    class MyDictionary<TKey, TValue> : MyIDictionary<TKey, TValue>
    {
        
        private readonly Dictionary<TKey, TValue> dictionary = new Dictionary<TKey, TValue>();

        public int Count { get => dictionary.Count; }

        public void Add(TKey key, TValue value)
        {
            if (key == null) throw new MyDictionaryException("Key cannot be null!");

            if (this.dictionary.ContainsKey(key)) throw new MyDictionaryException("Duplicate key!");

            dictionary.Add(key, value);
        }

        public bool ContainsKey(TKey key)
        {
            return this.dictionary.ContainsKey(key);
        }

        public bool Remove(TKey key)
        {
            if (key == null) throw new MyDictionaryException("Key cannot be null!");

            return dictionary.Remove(key);
        }

        public bool TryGetValue(TKey key, out TValue value)
        {
            if(key == null) throw new MyDictionaryException("Key cannot be null!");

            return dictionary.TryGetValue(key, out value);
        }

        public void Update(TKey key, TValue value)
        {
            if(key == null) throw new MyDictionaryException("Key cannot be null!");
            if(!dictionary.ContainsKey(key)) throw new MyDictionaryException("Key is not in the dictionary!");

            dictionary.Remove(key);
            dictionary.Add(key, value);
        }

        public Dictionary<TKey,TValue>.Enumerator GetEnumerator()
        {
            return dictionary.GetEnumerator();
        }

        public override string ToString()
        {
            StringBuilder builder = new StringBuilder();

            foreach(var item in dictionary)
            {
                builder.Append("{" + item.Key + ";" + item.Value + ")");
                builder.Append(System.Environment.NewLine);
            }

            return builder.ToString();
        }
    }
}
