#1
from ListQueue import *

def checkString(string):
    q1=ListQueue()
    i=0
    for i in range(len(string)):
        if (string[i]=="$"):
            break
        q1.enqueue(string[i])
    for j in range(i+1,len(string)):
        if q1.isEmpty():
            return False
        if (q1.front() != string[j]) :
            return False
        q1.dequeue()

    return q1.isEmpty()
    
result=checkString("abcd$abcd")
print(result)

#3






            