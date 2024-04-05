class ListStack:
    def __init__(self):
        self.__stack = []
    
    def push(self, x):
        self.__stack.append(x)
    
    def pop(self):
        return self.__stack.pop()
    
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__stack[-1]
    
    def isEmpty(self) -> bool:
        return not bool(self.__stack)
    
    def popAll(self):
        self.__stack.clear()
    
    def printStack(self):
        print("Stack from top:", end=' ')
        for i in range(len(self.__stack)-1, -1, -1):
            print(self.__stack[i], end=' ')
        print()
    
st1=ListStack()
st1.push(100)
st1.push(200)
print("Top is", st1.top())
st1.pop()
st1.push('Monday')
st1.printStack()
print("isEmpty?", st1.isEmpty())
