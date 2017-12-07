package Util.Heap;

import Util.Dictionary.MyIDictionary;

import java.util.Collection;

public interface IHeap {
    int allocate(int value);
    void deallocate(int address) throws HeapException;
    int getValue(int address) throws HeapException;
    void updateValue(int address,int value) throws HeapException;
    void garbageCollect(Collection<Integer> symbolTable) throws HeapException;
}
