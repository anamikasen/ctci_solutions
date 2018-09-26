class SingleArrayStacks(object):

    def __init__(self, stacksize = 100, number = 3):
        self.stacksize = stacksize
        self.number = number
        self.array = [None] * self.stacksize * self.number
        self.pointer = [-1] * self.number

    def push(self, stacknum, val):
        if self.pointer[stacknum] + 1 >= self.stacksize:
            print("Out of space")
        else:
            self.pointer[stacknum] += 1
            self.array[self.stacktop(stacknum)] = val

    def pop(self, stacknum, val):
        if self.pointer[stacknum] < 0:
            print("No stuff to pop")
        else:
            data = self.array[self.stacktop(stacknum)]
            self.array[self.stacktop(stacknum)]  = None
            self.pointer[stacknum] -= 1
            return data

    def peek(self, stacknum):
        if self.pointer[stacknum] < 0:
            print("No stuff")
        else:
            return self.array[self.stacktop(stacknum)]

    def isEmpty(self, stacknum):
        if self.pointer[stacknum] < 0:
            return True
        else:
            return False

    def stacktop(self, stacknum):
        return self.stacksize * stacknum + self.pointer[stacknum]


if __name__=="__main__":
    array = SingleArrayStacks()
    import pdb; pdb.set_trace()
