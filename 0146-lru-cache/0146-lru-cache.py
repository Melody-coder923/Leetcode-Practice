class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.size = 0
        # 哨兵节点
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # 从链表中断开节点（仅断链，不删 map，不改 size）
    def detach(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None

    # 将节点插入到尾部（最近使用）
    def add(self, node: Node, is_new: bool = True):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        if is_new:
            self.size += 1

    # 删除节点（用于超容量删除）
    def delete_node(self, node: Node):
        self.detach(node)
        del self.map[node.key]
        self.size -= 1

    # 移动节点到尾部（最近使用，不改变 size）
    def move_to_tail(self, node: Node):
        self.detach(node)
        self.add(node, is_new=False)

    # get 操作
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.move_to_tail(node)
        return node.val

    # put 操作
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.move_to_tail(node)
        else:
            if self.size == self.capacity:
                # 删除最久未使用的节点
                self.delete_node(self.head.next)
            new_node = Node(key, value)
            self.map[key] = new_node
            self.add(new_node, is_new=True)
