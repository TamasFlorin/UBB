namespace ToyLanguage.Util.Stack
{
    interface MyIStack<T>
    {
        void Push(T item);
        T Pop();
        bool IsEmpty
        {
            get;
        }
        T Peek();
    }
}
