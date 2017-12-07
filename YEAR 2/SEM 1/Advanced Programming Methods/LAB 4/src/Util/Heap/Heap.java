package Util.Heap;

import java.util.*;
import java.util.stream.Collectors;

public class Heap implements IHeap {
    private int currentCapacity = 16;
    private int nextList[];
    private final Map<Integer,Integer> values = new HashMap<>();
    private int currentFree;

    private void initNextList() {
        // we start at 1 because address 0 is considered NULL
        this.currentFree = 1;

        this.nextList = new int[this.currentCapacity];

        // set the next values
        for(int i = 0; i < nextList.length - 1;i++) {
            this.nextList[i] = i + 1;
        }

        // there is no next after the last value
        this.nextList[this.nextList.length - 1] = -1;
    }

    private void resize() {
        this.currentCapacity = this.currentCapacity * 2;
        //List<Integer> newNextList = new ArrayList<>(this.currentCapacity);
        //newNextList.addAll(this.nextList);
        int newNextList[] = Arrays.copyOf(this.nextList,this.currentCapacity);

        int oldSize = this.nextList.length;
        this.nextList = newNextList;

        // update new positions
        for(int i = oldSize - 1; i < newNextList.length; i++) {
            this.nextList[i] = i + 1;
        }

        // there is no next after the last value
        this.nextList[this.nextList.length - 1] = -1;

        // update current free position
        this.currentFree = oldSize - 1;
    }

    private void validateAddress(int address) throws HeapException {
        if( address <= 0) {
            throw new HeapException("Invalid address provided!");
        }

        if(!this.values.containsKey(address)) {
            throw new HeapException("Unallocated address provided!");
        }
    }

    public Heap() {
        this.initNextList();
    }

    @Override
    public int allocate(int value) {
        // check if we ran out of space
        if(this.currentFree == -1) {
            this.resize();
        }

        this.values.put(this.currentFree,value);
        int allocationAddress = this.currentFree;
        this.currentFree = this.nextList[this.currentFree];
        return allocationAddress;
    }

    @Override
    public void deallocate(int address) throws HeapException {
        validateAddress(address);

        // remove the given address
        this.values.remove(address);

        // update free position
        int freeAddress = this.currentFree;
        this.currentFree = address;
        this.nextList[address] = freeAddress;
    }

    @Override
    public int getValue(int address) throws HeapException {
        validateAddress(address);
        return this.values.get(address);
    }

    @Override
    public void updateValue(int address,int value) throws HeapException {
        validateAddress(address);
        this.values.put(address,value);
    }

    @Override
    public void garbageCollect(Collection<Integer> symTableValues) throws HeapException {
        Map<Integer,Integer> result = this.values.entrySet().stream().filter(e->symTableValues.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey,Map.Entry::getValue));

        // we are doing this because we also want
        // to free the positions of the removed
        // values
        for(Integer key : this.values.keySet()) {
            if(!result.containsKey(key)){
                this.deallocate(key);
            }
        }
    }

    @Override
    public String toString() {
        StringBuilder stringBuilder = new StringBuilder();

        for (Object o : this.values.entrySet()) {
            Map.Entry pair = (Map.Entry) o;
            stringBuilder.append("{").append(pair.getKey()).append("->").append(pair.getValue()).append("}");
            stringBuilder.append("\r\n");
        }

        return stringBuilder.toString();
    }
}
