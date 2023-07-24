"""
Leetcode 146: LRU Cache Eviction

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.hmap = {}  # dict maps from key -> value, Node's address

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        node = self.hmap[key]
        val = node.value
        # now extract and put this node at the end of the doubly linked list
        self.extract_and_append(node)
        return val

    def extract_and_append(self, node: Node):
        if self.size == 1 or self.tail == node:
            return
        # Extract a node from the doubly linked list
        p = node.prev
        n = node.next
        if p:
            p.next = n
        else:
            self.head = n
        if n:
            n.prev = p
        else:
            self.tail = p

        # Extract completed, now append a node at the end
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:  # update its value
            self.hmap[key].value = value
            node = self.hmap[key]
            self.extract_and_append(node)  # pull out the node and append at end of doubly linked list
            return

        # key doesn't exist in hmap
        node = Node(key, value)
        self.hmap[key] = node
        node.prev = self.tail
        if self.tail:  # if there's a tail
            self.tail.next = node  # link it to the new node
            self.tail = node  # update tail to newly added node
        else:
            self.head = node  # if there's no tail, which means no head either
            self.tail = node  # make them both point to new node
        self.size += 1  # update the size

        # if the size exceeds the capacity, then remove the head from linked list
        if self.size > self.capacity:
            # if size exceeds capacity, extract the front of the doubly linked list
            n = self.head.next  # second node to start of doubly linked list
            n.prev = None
            self.head.next = None
            del self.hmap[self.head.key]  # del from doubly linked list and hmap
            self.head = n
            self.size = self.capacity

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
