class Node():
    def __init__(self, val = None):
        self.val  = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
        self.tail = self.head
        self.len  = 0


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.len:
            return -1
        q   = self.head
        cur = 0
        while cur != index + 1:
            q   = q.next
            cur += 1
        return q.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        # new_node       = Node(val)
        # if self.head == self.tail:
        #     self.tail = new_node
        # new_node.next  = self.head.next
        # self.head.next = new_node
        # self.len       += 1
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.len, val)
        # new_node       = Node(val)
        # new_node.next  = self.tail.next
        # self.tail.next = new_node
        # self.tail      = new_node
        # self.len       += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.len:
            return
        if index < 0:
            index = 0
        

        cur = 0
        q   = self.head
        #! 注意这样等于 在 index - 1处
        while cur != index:
            q   = q.next
            cur += 1
        new_node      = Node(val)
        new_node.next = q.next
        q.next        = new_node
        self.len      += 1

            


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # 0 - index
        if index < 0 or index > self.len - 1:
            return
        q   = self.head.next
        pre = self.head
        cur = 0
        while q.next and cur != index:
            pre = q
            q   = q.next
            cur += 1
        pre.next = q.next
        self.len -= 1
        print(self)
    
    def __repr__(self):
        t = []
        q = self.head
        while q.next:
            q = q.next
            t.append(str(q.val))
        return '->'.join(t)





# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)