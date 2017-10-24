package Repository;

import java.util.Arrays;

public class MemoryRepository<E> implements IRepository<E> {
    private E[] data;
    private int size;
    private int capacity;

    public MemoryRepository() {
        this.capacity = 1;
        this.size = 0;

        // this will generate a warning
        // but as long as we do not return the data
        // we should be allright
        this.data = (E[]) new Object[this.capacity]; //
    }

    private void resize() {
        this.capacity = 2 * this.data.length;
        this.data = Arrays.copyOf(this.data,this.capacity);
    }

    private boolean isValidIndex(int index) {
        return index >=0 && index < this.size;
    }

    private void shiftLeft(int index) {
        for(int i = index; i < this.size - 1; i++) {
            this.data[i] = this.data[i+1];
        }

        this.size--;
    }

    @Override
    public void add(E element) throws DuplicateEntityException{
        int index = indexOf(element);

        // duplicate element
        if(isValidIndex(index))
            throw new DuplicateEntityException("The given entity is already in the repository!");

        if( this.size == this.capacity)
            this.resize();

        this.data[this.size++] = element;
    }

    @Override
    public void remove(Object o) throws EntityNotFoundException {
        int index = this.indexOf(o);

        if(!isValidIndex(index))
            throw new EntityNotFoundException("The given entity was not found!");

        this.shiftLeft(index);
    }

    @Override
    public int indexOf(Object o) {
        for(int i = 0; i < this.size; i++) {
            if( this.data[i].equals(o) )
                return i;
        }

        return -1;
    }

    @Override
    public E get(int index) throws IndexOutOfBoundsException {
        if(!isValidIndex(index))
            throw new IndexOutOfBoundsException("Index out of bounds!");

        return this.data[index];
    }

    @Override
    public E set(int index, E element) throws RepositoryException {
        if(!isValidIndex(index))
            throw new IndexOutOfBoundsException("Index out of bounds!");

        int duplicateIndex = indexOf(element);

        if(isValidIndex(duplicateIndex))
            throw new DuplicateEntityException("Duplicate entity!");

        E copy = this.data[index];
        this.data[index] = element;

        return copy;
    }

    @Override
    public int size() {
        return this.size;
    }
}
