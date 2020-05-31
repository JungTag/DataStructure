#front_index를 마련해 dequeue시간을 상수시간으로 관리하는 방법
class Queue:
    def __init__(self):
        self.items = []
        self.front_Index = 0
    def enqueue(self,val):
        self.items.append(val)
    def dequeue(self):
        if len(self.items) == 0 or self.front_Index == len(self.items):
            print("Queue is empty")
        else:
            x = self.items[self.front_Index]
            self.front_Index += 1
            return x
    def front(self):
        if len(self.items) == 0 or self.front_Index == len(self.items):
            print("Queue is empty")
        else:
            x = self.items[self.front_Index]
            return x
    def __len__(self):
        return len(self.items) - self.front_Index
    def isEmpty(self):
        return len(self)