package Util.Dictionary;

public interface MyIDictionary<K,V> {
    void put(K key,V value);
    boolean containsKey(Object key);
    V get(Object key);
    V remove(K key);
    boolean isEmpty();
}
