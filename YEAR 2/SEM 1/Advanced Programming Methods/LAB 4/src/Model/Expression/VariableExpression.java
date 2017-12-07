package Model.Expression;

import Util.Dictionary.MyIDictionary;
import Util.Heap.IHeap;

public class VariableExpression implements IExpression {
    private String name;

    public VariableExpression(String name){
        this.name = name;
    }

    @Override
    public int evaluate(MyIDictionary<String,Integer> symbolTable, IHeap heap) throws ExpressionException {
        if(symbolTable.containsKey(this.name))
            return symbolTable.get(this.name);

        throw new ExpressionException("No such symbol in the symbol table!");
    }

    @Override
    public String toString() {
        return "(" + this.name + ")";
    }
}
