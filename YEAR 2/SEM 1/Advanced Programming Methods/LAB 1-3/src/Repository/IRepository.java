package Repository;

public interface IRepository<E> {
    // add an element at the end of the list
    void add(E element) throws DuplicateEntityException;

    // remove an element
    void remove(Object o) throws EntityNotFoundException;

    // returns the element at the given index
    E get(int index) throws IndexOutOfBoundsException;

    // returns the index of an element if present
    // -1 otherwise
    int indexOf(Object o);

    // set the element at the given index to the given value
    E set(int index,E element) throws RepositoryException;

    int size();
}
