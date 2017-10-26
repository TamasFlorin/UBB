package Model.Statement;

import Model.Expression.ExpressionException;
import Model.State.ProgramState;

import java.io.FileNotFoundException;
import java.io.IOException;

public interface IStatement {
    ProgramState execute(ProgramState programState) throws ExpressionException, StatementException, IOException;
}
