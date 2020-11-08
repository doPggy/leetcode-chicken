class Node():
    def __init__(self, val = None):
        self.next = None
        self.pre  = None
        self.val  = val

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head      = Node()
        self.tail      = Node()
        self.head.next = self.tail
        self.tail.pre  = self.head
        self.len       = 0


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # >= 才行
        if index < 0 or index >= self.len:
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
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.len, val)


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.len:
            return
        elif index < 0:
            index = 0
        q   = self.head
        cur = 0
        # 直接扦插法
        while cur != index + 1:
            q   = q.next
            cur += 1
        new_node      = Node(val)
        new_node.next = q
        new_node.pre  = q.pre
        q.pre.next = new_node
        q.pre      = new_node
        self.len   += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # index >= 还是 >
        if index < 0 or index >= self.len:
            return
        q   = self.head
        cur = 0
        print(self)
        print(index + 1)
        while cur != index + 1:
            q   = q.next
            cur += 1
        q.pre.next = q.next
        q.next.pre = q.pre
        self.len   -= 1


    def __repr__(self):
        t = []
        q = self.head
        while q.next:
            q = q.next
            t.append(str(q.val))
        return '<->'.join(t)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)