class LinkedListDict:
    class LinkedList:
        __slots__ = 'key', 'value', 'prev', 'follow'

        def __init__(self, key=None, value=None, prev=None, follow=None):
            self.key = key
            self.value = value
            self.prev = prev
            self.follow = follow

    def __init__(self):
        self._dict = {}
        self._head = self.LinkedList()
        self._tail = self.LinkedList()
        self._connect(self._head, self._tail)

    def __len__(self):
        return len(self._dict)

    def __getitem__(self, key):
        if key in self._dict:
            node = self._dict[key]
            self.move_to_back(node)
            return node.value
        return -1

    def __setitem__(self, key, value):
        if key in self._dict:
            node = self._dict[key]
            self.move_to_back(node)
            node.value = value
        else:
            self._dict[key] = self.LinkedList(key, value)
            node = self._dict[key]
            self._connect(self._tail.prev, node)
            self._connect(node, self._tail)

    def __contains__(self, key):
        return key in self._dict

    def popfirst(self):
        node = self._head.follow
        self._connect(node.prev, node.follow)
        del self._dict[node.key]

    def _connect(self, node1, node2):
        node1.follow, node2.prev = node2, node1

    def move_to_back(self, node):
        self._connect(node.prev, node.follow)
        self._connect(self._tail.prev, node)
        self._connect(node, self._tail)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = LinkedListDict()

    def get(self, key: int) -> int:
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.data and len(self.data) == self.capacity:
            self.data.popfirst()
        self.data[key] = value

