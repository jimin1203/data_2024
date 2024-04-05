class ListQueue:
    def __init__(self):
        self.__queue=[]
    
    def enqueue(self, x):
        self.__queue.append(x)

    def dequeue(self):
        return self.__queue.pop(0)
    
    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.__queue[0]
    
    def isEmpty(self) -> bool :
        return (len(self.__queue)==0)
    
    def dequeueAll(self):
        self.__queue.clear()
    
    def printQueue(self):
        print("Queue from front:", end=' ')
        for i in range(len(self.__queue)):
            print(self.__queue[i], end=' ')
        print()
        
    def stack_push(x):

q2 = ListQueue()
q2.enqueue("Mon")
q2.enqueue("Tue")
q2.enqueue(1234)
q2.enqueue("Wed")
q2.dequeue()
q2.enqueue("aaa")
q2.printQueue()