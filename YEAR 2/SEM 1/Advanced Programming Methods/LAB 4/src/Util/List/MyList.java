package Util.List;

import java.util.ArrayList;
import java.util.List;

public class MyList<E> implements MyIList<E> {
    private List<E> list;

    public MyList() {
        this.list = new ArrayList<>();
    }

    private boolean validIndex(int index) {
        return index >=0 && index < this.list.size();
    }

    @Override
    public void add(E element) {
        this.list.add(element);
    }

    @Override
    public boolean remove(Object o) {
        return this.list.remove(o);
    }

    @Override
    public int indexOf(Object o) {
        return this.list.indexOf(o);
    }

    @Override
    public E get(int index) throws ListException {
        if(!validIndex(index))
            throw new ListException("Index is out of bounds!");

        return this.list.get(index);
    }

    @Override
    public E set(int index, E element) throws ListException {
        if(!validIndex(index))
            throw new ListException("Index is out of bounds!");

        return this.list.set(index,element);
    }

    @Override
    public int size() {
        return this.list.size();
    }

    @Override
    public String toString() {
        StringBuilder stringBuilder = new StringBuilder();

        for(E element : this.list) {
            stringBuilder.append(element);
            stringBuilder.append("\r\n");
        }

        return stringBuilder.toString();
    }
}
