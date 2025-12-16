
class Node:
    """节点类，存储 key, value, freq，以及双向链表指针"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1  # 新节点插入时 freq = 1
        self.prev = None
        self.next = None


class DoubleLinkedList:
    """双向链表类，用于存储相同频率的节点"""
    def __init__(self):
        # 创建 dummy head & tail 节点，方便插入和删除
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self):
        return self.head.next == self.tail

    def add_to_tail(self, node):
        """把节点加到链表尾部（表示最近使用）"""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        """从链表中删除节点"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_head(self):
        """删除链表头节点（最久未使用），返回该节点"""
        if self.isEmpty():
            return None
        node = self.head.next
        self.remove(node)
        return node


class LFUCache:
    """
    LFU Cache 数据结构
    核心思想：
    - nodeMap: key -> Node，用于 O(1) 查找节点
    - freqMap: freq -> 双向链表，存储相同 freq 的节点
    - minFreq: 当前缓存中的最小频率，用于 O(1) 淘汰
    """
    """

    nodeMap : key  → node
    node    : { key, value, freq }

    freqMap : freq → 双向链表（node）
          （链表头 = 最旧，尾 = 最新）
    minFreq : 当前缓存中的最小频率
    当要淘汰节点时：直接找 minFreq, 删除 freqMap[minFreq] 链表头节点
    key:freq  value:双向链表

    所以LFU Cache 里最终会有 四样东西:
    nodeMap : key  → node
    
    freqMap : freq → 双向链表（node）
    minFreq : 当前最小频率   ← 这个就是“额外变量”
    capacity / size : 容量和当前大小
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.nodeMap = {}       # key -> Node
        self.freqMap = {}       # freq -> DoubleLinkedList
        self.minFreq = 0

    def _update_freq(self, node: Node):
        """内部函数：节点访问或更新时更新频率"""
        freq = node.freq
        # 从原 freq 链表删除
        self.freqMap[freq].remove(node)

        # 如果原 freq 链表空了，并且 freq == minFreq，则 minFreq +1
        if self.freqMap[freq].isEmpty():
            del self.freqMap[freq]  # 清理空链表
            if freq == self.minFreq:
                self.minFreq += 1

        # freq +1
        node.freq += 1
        # 放到新 freq 链表尾部
        if node.freq not in self.freqMap:
            self.freqMap[node.freq] = DoubleLinkedList()
        self.freqMap[node.freq].add_to_tail(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        # 更新频率
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodeMap:
            # key 已存在，更新值并更新频率
            node = self.nodeMap[key]
            node.value = value
            self._update_freq(node)
        else:
            # key 不存在，需要插入新节点
            if self.size == self.capacity:
                # 容量满了，淘汰 minFreq 链表头节点（最久未使用的节点）
                old_list = self.freqMap[self.minFreq]
                node_to_remove = old_list.remove_head()
                del self.nodeMap[node_to_remove.key]
                if old_list.isEmpty():
                    del self.freqMap[self.minFreq]
                self.size -= 1

            # 插入新节点
            new_node = Node(key, value)
            self.nodeMap[key] = new_node
            if 1 not in self.freqMap:
                self.freqMap[1] = DoubleLinkedList()
            self.freqMap[1].add_to_tail(new_node)
            self.minFreq = 1  # 新节点 freq = 1，更新 minFreq
            self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)