package Util.Stack;

public interface MyIStack<E> {
    void push(E element);
    E pop() throws StackException;
    boolean isEmpty();
}
