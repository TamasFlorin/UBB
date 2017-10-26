package Util.Dictionary;

import java.util.Collection;

public interface MyIDictionary<K,V> {
    void put(K key,V value);
    boolean containsKey(Object key);
    boolean containsValue(Object value);
    V get(Object key);
    V remove(K key);
    Collection<V> values();
    boolean isEmpty();
    int size();
}
