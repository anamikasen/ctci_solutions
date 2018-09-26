class StackOfPlates:

    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, val):
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(val)

    def pop(self):
        if self.stacks[-1] is None:
            return None
        else:
            data = self.stacks[-1].pop()
            if len(self.stacks[-1]) == 0:
                self.stacks.pop()

    def popAtIndex(self, substack):
        if len(self.stacks)+1 < substack:
            print('Substack does not exist')
        else:
            if len(self.stacks[substack-1]) == self.capacity:
                print("Stack full")
            else:
                self.stacks[substack-1].pop()


def test():
    setofstacks = StackOfPlates(8)
    for i in range(24):
        setofstacks.push(i)
        print(i)

    for i in range(5):
        print ("Popped", setofstacks.pop())

    print("Test for popAt")
    for i in range(5):
        for i in range(3):
            print ("Popped", setofstacks.popAtIndex(i+1))


if __name__ == "__main__":
    test()
