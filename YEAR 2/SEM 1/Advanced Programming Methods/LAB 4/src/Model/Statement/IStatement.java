package Model.Statement;

import Model.Expression.ExpressionException;
import Model.State.ProgramState;

public interface IStatement {
    ProgramState execute(ProgramState programState) throws ExpressionException;
}
