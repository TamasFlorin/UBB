package Repository;

import Model.State.ProgramState;

public interface IRepository<E> {
    void add(E element);
    E back() throws RepositoryException;
}
