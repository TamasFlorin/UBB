package Repository;

import Model.State.ProgramState;

public interface IRepository {
    void add(ProgramState state);
    ProgramState back() throws RepositoryException;
    void logData() throws RepositoryException;
}
