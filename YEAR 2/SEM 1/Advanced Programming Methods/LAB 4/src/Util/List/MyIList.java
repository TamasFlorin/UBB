package Util.List;

public interface MyIList<E> {
    // add an element at the end of the list
    void add(E element);

    // remove an element
    boolean remove(Object o);

    // returns the element at the given index
    E get(int index) throws ListException;

    // returns the index of an element if present
    // -1 otherwise
    int indexOf(Object o);

    // set the element at the given index to the given value
    E set(int index,E element) throws ListException;

    int size();
}
