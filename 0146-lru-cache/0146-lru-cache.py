class Node:
    def __init__(self, key, val):
        # DLL Node
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(-1, -1)
        # random val, we know that this is invalid
        # head.next will be the actual node
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        # return and push to top so that we do not clear it
        # LRU
        node = self.dic[key]
        self.remove(node)
        self.add(node)
        # gets added to the top of priority (end of our LL)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)
            # but we don't have to del from dict since we update it next
        
        node = Node(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            # remove from least recently used - top of DLL near head
            node_to_del = self.head.next
            self.remove(node_to_del)
            del self.dic[node_to_del.key]

    def add(self, node):
        # add to back
        high_priority = self.tail.prev
        high_priority.next = node
        node.prev = high_priority

        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)