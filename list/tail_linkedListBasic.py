from listNode import ListNode

class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__tail = self.__head  # tail 노드 추가
        self.__numItems = 0

    def insert(self, i: int, newItem):
        if i >= 0 and i <= self.__numItems:
            if i == 0:
                newNode = ListNode(newItem, self.__head.next)
                self.__head.next = newNode
                if self.__tail == self.__head:  # 리스트가 비어있을 경우 tail 업데이트
                    self.__tail = newNode
            else:
                prev = self.__getNode(i - 1)
                newNode = ListNode(newItem, prev.next)
                prev.next = newNode
                if prev == self.__tail:  # 삽입 후 tail을 업데이트
                    self.__tail = newNode
            self.__numItems += 1 
        else:
            print("index", i, ": out of bound in insert()")

    def append(self, newItem):
        newNode = ListNode(newItem, None)
        self.__tail.next = newNode
        self.__tail = newNode  # 새로운 노드를 tail로 설정
        self.__numItems += 1

    def pop(self, i: int):
        if i >= 0 and i < self.__numItems:
            prev = self.__getNode(i - 1)
            curr = prev.next
            prev.next = curr.next
            if curr == self.__tail:  # 삭제 후 tail을 업데이트
                self.__tail = prev
            retItem = curr.item
            self.__numItems -= 1
            return retItem
        else:
            return None

    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            if curr == self.__tail:  # 삭제 후 tail을 업데이트
                self.__tail = prev
            self.__numItems -= 1
        else:
            return None

    def get(self, i: int):
        if self.isEmpty():
            return None
        if i >= 0 and i < self.__numItems:
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
        self.__tail = self.__head  # tail 노드 초기화
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
        a = []
        for index in range(self.__numItems):
            a.append(self.get(index))
        a.sort()
        self.clear()
        for index in range(len(a)):
            self.append(a[index])

    def __findNode(self, x) -> (ListNode, ListNode):
        iterator = self.__head
        for _ in range(self.__numItems):
            if iterator.next.item == x:
                return (iterator, iterator.next)
            iterator = iterator.next
        return (None, None)

    def __getNode(self, i: int) -> ListNode:
        curr = self.__head.next
        for index in range(i):
            curr = curr.next
        return curr

    def printList(self):
        curr = self.__head.next
        while curr != None:
            print(curr.item, end=' ')
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


# 테스트 코드
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
