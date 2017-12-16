package Repository;

import Model.State.ProgramState;
import java.util.List;

public interface IRepository {
    void add(ProgramState state);
    ProgramState back() throws RepositoryException;
    void logData() throws RepositoryException;
    List<ProgramState> getAll();
    void setData(List<ProgramState> states);
}
