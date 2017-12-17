namespace ToyLanguage.Util.List
{
    interface MyIList<T>
    {
        void Add(T item);
        T ElementAt(int index);
        int Count
        {
            get;
        }
    }
}
