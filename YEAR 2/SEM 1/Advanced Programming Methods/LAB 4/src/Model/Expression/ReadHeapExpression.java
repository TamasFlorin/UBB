package Model.Expression;

import Util.Dictionary.MyIDictionary;
import Util.Heap.HeapException;
import Util.Heap.IHeap;

public class ReadHeapExpression implements IExpression {
    private final String variableName;

    public ReadHeapExpression(String variableName) {
        this.variableName = variableName;
    }

    @Override
    public int evaluate(MyIDictionary<String, Integer> symbolTable, IHeap heap) throws ExpressionException {
        int address = symbolTable.get(variableName);
        try {
            return heap.getValue(address);
        }catch (HeapException e) {
            throw new ExpressionException(e.getMessage());
        }
    }

    @Override
    public String toString() {
        return "ReadHeapExpression(" + this.variableName + ")";
    }
}
