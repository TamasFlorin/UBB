using System.Collections.Generic;

namespace ToyLanguage.Util.Dictionary
{
    interface MyIDictionary<TKey,TValue>
    {
        void Add(TKey key, TValue value);
        bool Remove(TKey key);
        int Count
        {
            get;
        }

        bool ContainsKey(TKey key);

        void Update(TKey key,TValue value);

        bool TryGetValue(TKey key, out TValue value);

        Dictionary<TKey, TValue>.Enumerator GetEnumerator();
    }
}
