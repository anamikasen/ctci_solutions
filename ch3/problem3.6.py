class sortStacks(list):

    def peek(self):
        print(self[len(self)-1])

    def isEmpty(self):
        print(len(self)==0)

    def prnt(self):
        for items in self:
            print(items)

    def push(self, val):
        self.append(val)

    def pop(self):
        print(self[len(self)-1])
        self[len(self)-1] = None

    def sort(self):
        

if __name__=="__main__":
    stack = sortStacks([1, 8, 5, 9])
    stack.prnt()
    stack.peek()
    stack.isEmpty()
    stack.pop()
    stack.prnt()
    stack.push(36)
    stack.prnt()
