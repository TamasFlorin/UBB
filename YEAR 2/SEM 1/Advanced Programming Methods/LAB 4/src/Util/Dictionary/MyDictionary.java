package Util.Dictionary;

import java.util.HashMap;
import java.util.Map;

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
    public boolean isEmpty() {
        return dictionary.isEmpty();
    }

    @Override
    public V remove(K key) {
        return dictionary.remove(key);
    }
}
