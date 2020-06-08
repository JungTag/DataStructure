class Node:
    def __init__(self,key): #value를 넣고자 할 때는 매개변수에 value = None추가!!
        self.key = key
        #self.value = value
        self.next = None
    def __str__(self):
        return str(self.key)
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def printList(self): 
        v = self.head
        while(v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")
		
    def __len__(self):
        return self.size
    
    def pushFront(self,key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def pushBack(self,key): #경우 2가지
        new_node = Node(key)
        if self.head == None: #빈리스트인 경우
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1
     
   
    def popFront(self): #경우 2가지
        if self.head == None: #빈 리스트인 경우
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1 
            del x
            return key
		# head 노드의 값 리턴. empty list이면 None 리턴

    def popBack(self): #*경우 3가지!!!*
        if self.head == None: #빈 리스트인 경우
            return None
        else:
            prev = None
            tail = self.head
            while tail.next != None: #tail을 노드 맨 끝으로 옮긴다
                prev = tail
                tail = tail.next
            if prev == None: #리스트에 노드가 하나인 경우(prev(0)-tail(head)-tail.next(0))
                self.head = None
            else: #일반적인 경우
                prev.next = tail.next #tail.next = None
            key = tail.key
            self.size -= 1
            del tail
            return key # tail 노드의 값 리턴. empty list이면 None 리턴

    def search(self, key):
        v = self.head
        while v != None: # = while v: 
            if v.key == key:
                return v
            v = v.next
        return None # key 값을 저장된 노드 리턴. 없으면 None 리턴

    def remove(self, x): #*3가지 경우* -> (1)빈 리스트 (2)노드x가 헤드노드 (3)일반적인 경우
        if self.head == None: #(1)빈 리스트
            return False
        else:
            prev = self.head
            if prev == x:
                self.popFront() #(2)노드x가 헤드노드
                return True
            else:
                while prev.next != None: #일반적인 경우
                    if prev.next == x:
                        prev.next = x.next
                        self.size -= 1
                        del x
                        return True
                    prev = prev.next
                return False #반복문 내에서 못찾으면 False반환
			    # 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴

			    
# Big-O
# pushFront: O(1), pushBack: O(n), popFront: O(1), popBack: O(n), search: O(n), remove: O(n)
