class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def enqueue(self, val):
        self.stack1.append(val)

    def dequeue(self):
        if len(self.stack1)==0:
            return None

        for i in range(len(self.stack1)):
            data = self.stack1.pop()
            self.stack2.append(data)

        ans = self.stack2.pop()

        for items in self.stack2:
            data = self.stack2.pop()
            self.stack1.append(data)

        return ans

    def prnt(self):
        print(self.stack1)
        print(self.stack2)


if __name__=="__main__":
    Q = MyQueue()
    Q.enqueue(5)
    Q.enqueue(6)
    Q.dequeue()
    import pdb; pdb.set_trace()
    Q.prnt()
