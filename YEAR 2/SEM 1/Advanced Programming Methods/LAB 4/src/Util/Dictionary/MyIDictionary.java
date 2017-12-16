package Util.Dictionary;

import java.util.Collection;
import java.util.Map;
import java.util.Set;

public interface MyIDictionary<K,V> {
    void put(K key,V value);
    boolean containsKey(Object key);
    boolean containsValue(Object value);
    V get(Object key);
    V remove(K key);
    Collection<V> values();
    boolean isEmpty();
    int size();
    Set<Map.Entry<K,V>> entrySet();
    void clear();
}
