package Util.Dictionary;

import java.util.*;

public class MyDictionary<K,V> implements MyIDictionary<K,V> {
    private Map<K,V> dictionary;

    public MyDictionary() {
        dictionary = new HashMap<>();
    }

    @Override
    public void put(K key, V value) {
        dictionary.put(key,value);
    }

    @Override
    public V get(Object key) {
        return dictionary.get(key);
    }

    @Override
    public boolean containsKey(Object key) {
        return dictionary.containsKey(key);
    }

    @Override
    public boolean containsValue(Object value) {
        return dictionary.containsValue(value);
    }

    @Override
    public boolean isEmpty() {
        return dictionary.isEmpty();
    }

    @Override
    public V remove(K key) {
        return dictionary.remove(key);
    }

    @Override
    public String toString() {
        StringBuilder stringBuilder = new StringBuilder();

        for (Object o : this.dictionary.entrySet()) {
            Map.Entry pair = (Map.Entry) o;
            stringBuilder.append("{").append(pair.getKey()).append(";").append(pair.getValue()).append("}");
            stringBuilder.append("\r\n");
        }

        return stringBuilder.toString();
    }

    @Override
    public int size() {
        return this.dictionary.size();
    }

    @Override
    public Collection<V> values() {
        return this.dictionary.values();
    }
}
