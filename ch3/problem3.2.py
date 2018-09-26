class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, val):
        if self.size(self.items) == 0:
            self.min = val
            self.items.append(val)
        else:
            if self.min > val:
                self.min = val
            self.items.append(val)

    def pop(self):
        if self.size(self.items) == 0:
            print('Nothing to pop')
        else:
            return self.items[self.size(self.items)-1]

    def getMin(self):
        if self.size(self.items)==0:
            return ("No elements")
        else:
            return self.min

    def size(self, items):
        return len(self.items)


if __name__=="__main__":
    stacks = Stack()
    import pdb; pdb.set_trace()
