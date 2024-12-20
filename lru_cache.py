class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:    
    def __init__(self, capacity: int=16):
        self.capacity = capacity
        self.cache = dict()
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def __remove(self, node: Node) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def __insert(self, node: Node) -> None:
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev
    
    def put(self, key, value) -> None:
        if key in self.cache:
            self.__remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.__insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.__remove(lru)
            del self.cache[lru.key] 
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.__remove(node)
            self.__insert(node)
            return node.val
        return None

        
    
    
