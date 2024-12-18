class MyLinkedList {
    
    private class ListNode {
        ListNode next;
        ListNode prev;
        int val;

        ListNode() {
        }
        
        ListNode(int val, ListNode next, ListNode prev) {
            this.val = val;
            this.next = next;
            this.prev = prev;
        }
    }
    
    ListNode dummyHead = new ListNode();
    ListNode dummyTail = new ListNode();
    
    int size;
    
    public MyLinkedList() {
        dummyHead.next = dummyTail;
        dummyTail.prev = dummyHead;
    }
    
    public int get(int index) {
        if (index >= size || index < 0) {
            return -1;
        }
                
        return getNode(index).val;
    }
    
    public void addAtHead(int val) {              
        addNewNodeAfter(dummyHead, val);
    }
    
    public void addAtTail(int val) {
        addNewNodeBefore(dummyTail, val);
    }
    
    public void addAtIndex(int index, int val) {
        if (index == 0) {
            addAtHead(val);
            return ;
        }
        else if (index == size) {
            addAtTail(val);
            return ;
        }
        else if (index < 0 || index > size) {
            return ;
        }
        
        addNewNodeBefore(getNode(index), val);
    }
    
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return ;
        }
        
        var current = getNode(index);
        current.prev.next = current.next;
        current.next.prev = current.prev;
        size--;
    }
    
    private ListNode getNode(int index) {
        var current = (ListNode)null;
        
        if (index < size / 2) {
            current = dummyHead.next;
            for (int i = 0; i < index; i++) {
                current = current.next;
            }
        }
        else {
            current = dummyTail.prev;
            for (int i = 0; i < size - index - 1; i++) {
                current = current.prev;
            }
        }
        
        return current;
    }
    
    private void addNewNodeAfter(ListNode node, int val) {
        var newNode = new ListNode(val, node.next, node);

        node.next.prev = newNode;
        node.next = newNode;
        
        size++;
    }
    
    private void addNewNodeBefore(ListNode node, int val) {
        var newNode = new ListNode(val, node, node.prev);

        node.prev.next = newNode;
        node.prev = newNode;

        size++;
    }
}