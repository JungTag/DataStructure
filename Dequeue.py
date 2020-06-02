class Dequeue:
    def __init__(self, str):
        self.items = list(str)
    def append(self, v):
        self.items.append(v)
    def appendleft(self, v):
        self.items.insert(0, v)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Dequeue is empty")
    def popleft(self):
        try:
            return self.items.pop(0)
        except IndexError:
            print("Dequeue is empty")
    def right(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Dequeue is empty")
    def left(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Dequeue is empty")
    def __len__(self):
        return len(self.items)