#리스트를 이용한 구현
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,val):
        self.items.append(val)
    def dequeue(self):
        try:
            return self.items.pop(0)
        except IndexError:
            print("Queue is empty")
    def front(self):
        try:
            return self.items[0]
        except IndexError:
            print("Queue is empty")
    def __len__(self):
        return len(self.items)
    def isEmpty(self):
        return len(self)
