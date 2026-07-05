    Stack<ListNode> stack = new Stack<>();
    ListNode node = head;
    
    while(node != null) {
        stack.add(node);
        node = node.next;
    }
    
    node = head;
    
    while(node != null) {
        ListNode next = node.next;
        ListNode endNode = stack.pop();
        
        node.next = endNode;
        endNode.next = next;
        node = next;
        if(node != null && node.next == endNode) {
            node.next = null;
            break;
        }
    }
    
}