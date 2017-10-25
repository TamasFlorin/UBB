package Repository;

import java.util.ArrayList;
import java.util.List;

public class MemoryRepository<E> implements IRepository<E> {
    private List<E> list;

    public MemoryRepository() {
        this.list = new ArrayList<>();
    }

    @Override
    public void add(E element) {
        this.list.add(element);
    }

    @Override
    public E back() throws RepositoryException {
        if( this.list.size() == 0)
            throw new RepositoryException("Empty repository!");

        return this.list.get(this.list.size() - 1);
    }
}
