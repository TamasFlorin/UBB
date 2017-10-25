package Util.Stack;

import java.util.Stack;

public class MyStack<E> implements MyIStack<E> {
    private Stack<E> stack;

    public MyStack() {
        this.stack = new Stack<>();
    }

    @Override
    public void push(E element) {
        this.stack.push(element);
    }

    @Override
    public E pop() throws StackException {
        if(this.isEmpty())
            throw new StackException("Cannot pop from empty stack!");

        return this.stack.pop();
    }

    @Override
    public boolean isEmpty() {
        return this.stack.isEmpty();
    }
}
