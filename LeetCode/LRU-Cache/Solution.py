class DListNode {
public:
    int key, val;
    DListNode *prev, *next;

    DListNode(int key = 0, int val = 0, DListNode* prev = nullptr, DListNode* next = nullptr)
    : key(key), val(val), prev(prev), next(next) {}
};

class DLinkedList {
public:
    int size;
    DListNode *head, *tail;

    DLinkedList() : size(0) {
        head = new DListNode(-1, -1);
        head->next = tail = new DListNode(-1, -1, head);
    }

    void append(DListNode* node) {
        tail->prev->next = node;
        node->prev = tail->prev;
        node->next = tail;
        tail->prev = node;
        size++;
    }

    void erase(DListNode* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
        size--;
    }

    ~DLinkedList() {
        DListNode *curr = head, *cnext;
        while (curr) {
            cnext = curr->next;
            delete curr;
            curr = cnext;
        }
    }
};

class LRUCache {
private:
    int capacity;
    unordered_map<int, DListNode*> keyNode;
    DLinkedList list;

public:
    LRUCache(int capacity) : capacity(capacity) {}
    
    int get(int key) {
        if (keyNode.find(key) == keyNode.end()) {
            return -1;
        }
        DListNode* node = keyNode[key];
        list.erase(node);
        list.append(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (keyNode.find(key) != keyNode.end()) {
            list.erase(keyNode[key]);
        } else if (list.size == capacity) {
            DListNode* lru = list.head->next;
            list.erase(lru);
            keyNode.erase(lru->key);
            delete lru;
        }
        DListNode* node = new DListNode(key, value);
        list.append(node);
        keyNode[key] = node;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */