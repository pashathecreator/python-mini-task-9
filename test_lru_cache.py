import pytest
from lru_cache import LRUCache

def test_put_and_get():
    cache = LRUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1 
    cache.put(3, 3)  
    assert cache.get(2) is None 
    assert cache.get(3) == 3 
    cache.put(4, 4)  
    assert cache.get(1) is None  
    assert cache.get(4) == 4  

def test_update_existing_key():
    cache = LRUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10) 
    assert cache.get(1) == 10 
    assert cache.get(2) == 2  

def test_lru_eviction():
    cache = LRUCache(capacity=3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.get(1)  
    cache.put(4, 4)  
    assert cache.get(2) is None 
    assert cache.get(1) == 1 
    assert cache.get(3) == 3  
    assert cache.get(4) == 4  

def test_empty_cache():
    cache = LRUCache(capacity=2)
    assert cache.get(1) is None  

def test_overwrite_existing_key():
    cache = LRUCache(capacity=2)
    cache.put(1, 1)
    cache.put(1, 10)  
    assert cache.get(1) == 10 

def test_capacity_one():
    cache = LRUCache(capacity=1)
    cache.put(1, 1)
    assert cache.get(1) == 1 
    cache.put(2, 2)  
    assert cache.get(1) is None  
    assert cache.get(2) == 2 
    
def test_ordering():
    cache = LRUCache(capacity=3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.get(2)  
    cache.put(4, 4)  
    assert cache.get(1) is None  
    assert cache.get(2) == 2  
    assert cache.get(3) == 3 
    assert cache.get(4) == 4  

def test_put_after_eviction():
    cache = LRUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)  
    cache.put(4, 4)  
    assert cache.get(1) is None 
