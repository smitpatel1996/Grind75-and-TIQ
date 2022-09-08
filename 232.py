#Implement Queue using Stacks

#Approach : Stacks and Queues
#TC : O(n), SC: O(n)
class MyQueue:
    def __init__(self):
        self.pushStack, self.popStack = [],[]
    def push(self, x: int):
        self.pushStack.append(x)
    def pop(self):
        if(not len(self.popStack)):
            while(len(self.pushStack)):
                self.popStack.append(self.pushStack.pop())
        return self.popStack.pop()
    def peek(self):
        if(len(self.popStack)): return self.popStack[-1]
        else: return self.pushStack[0]
    def empty(self):
        return not (len(self.popStack) or len(self.pushStack))