from listNode import ListNode

class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0

 
    # [알고리즘 5- 2] 구현: 연결 리스트에 원소 삽입하기 (더미 헤드를 두는 대표 버전)
    def insert(self, i:int, newItem) :
        if i >= 0 and i <= self.__numItems:
            prev = self.__getNode(i - 1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1 
        else:
            print("index", i, ": out of bound in insert()") # 필요 시 에러 처리

    def append (self, newItem):
        prev = self.__getNode(self.__numItems - 1)
        newNode = ListNode(newItem, prev.next)
        prev.next = newNode
        self.__numItems += 1

    # [알고리즘 5-3] 구현: 연결 리스트의 원소 삭제하기 
    def pop(self, i:int):
        if i == -1:  # 마지막 원소 제거
            i = self.__numItems - 1
        if (i >= 0 and i <= self.__numItems-1):
            prev = self.__getNode(i-1)
            curr = prev.next
            prev.next = curr.next
            retItem = curr.item
            self.__numItems -= 1
            return retItem
        else :
            return None
    
    # [알고리즘 5-4] 구현: 연결 리스트의 원소 x 삭제하기 (더미 헤드를 두는 대표 버전)
    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            self.__numItems -= 1
        else:
            return None
        
    def get(self, i:int):
        if self.isEmpty():
            return None
        if ( i>= 0 and i <= self.__numItems - 1):
            return self.__getNode(i).item
        else:
            return None
    
    def index(self, x) -> int:
        curr = self.__head.next
        for index in range(self.__numItems):
            if curr.item == x:
                return index
            else:
                curr = curr.next
        return -2

    def isEmpty(self) -> bool:
        return self.__numItems == 0
    
    def size(self) -> int:
        return self.__numItems
    
    def clear(self):
        self.__head = ListNode("dummy", None)
        self.__numItems = 0
    
    def count(self, x) -> int:
        cnt = 0
        curr = self.__head.next
        while curr != None:
            if curr.item == x:
                cnt += 1
            curr = curr.next
        return cnt
    
    def extend(self, a):
        for index in range(a.size()):
            self.append(a.get(index))

    def copy(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.append(self.get(index))
        return a
    
    def reverse(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.insert(0, self.get(index))
        self.clear()
        for index in range(a.size()):
            self.append(a.get(index))

    def sort(self) -> None:
        a=[]
        for index in range(self.__numItems):      
            a.append(self.get(index))
        a.sort()
        self.clear()
        for index in range(len(a)):
            self.append(a[index])
    
    def __findNode(self, x):
        prev = self.__head
        curr = prev.next
        while curr is not None:
            if curr.item == x:
                return (prev, curr)
            prev = curr
            curr = curr.next
        return (None, None)  # x를 찾지 못한 경우

    
    def __getNode(self, i:int) -> ListNode:
        curr = self.__head
        for index in range(i+1):
            curr = curr.next
        return curr
    
    def printList(self):
        curr = self.__head.next
        while curr != None:
            print(curr.item, end = ' ')
            curr = curr.next
        print()
    
    def __iter__(self):
        self.current = self.__head.next
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.item
            self.current = self.current.next
            return data
        
list = LinkedListBasic()
list.append(30)
list.insert(0, 20)

a = LinkedListBasic()
a.append(4)
a.append(3)
a.append(3)
a.append(2)
a.append(1)

list.extend(a)
list.reverse()
list.pop(0)

print("count(3):", list.count(3))
print("get(2):", list.get(2))

list.printList()