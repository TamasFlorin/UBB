package Util.Stack;

import java.util.Stack;

public interface MyIStack<E> {
    void push(E element);
    E pop() throws StackException;
    boolean isEmpty();
    E top() throws StackException;
}
