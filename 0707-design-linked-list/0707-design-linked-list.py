class MyLinkedList:

    def __init__(self):
        self.vals = []
        

    def get(self, index: int) -> int:
        if index >= len(self.vals):
            return -1
        return self.vals[index]
        

    def addAtHead(self, val: int) -> None:
        self.vals.insert(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.vals.insert(len(self.vals), val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > len(self.vals):
            return
        self.vals.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if index >= len(self.vals):
            return
        
        del self.vals[index] 
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)