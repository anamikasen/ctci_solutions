class TowerOfHanoi:

    def __init__(self, size):
        self.size = size
        self.towers = [[], [], []]
        self.towers[0] = [x for x in range(size, 0, -1)]

    def move(self):
        if len(self.towers[0]) == 1:
            data = self.towers[0].pop()
            self.towers[-1].append(data)
        else:
            self.moveagain(0, 1)
            self.moveagain(1, 2)

    def moveagain(self, frm, to):
        for i in range(self.size):
            data = self.towers[frm].pop()
            self.towers[to].append(data)


if __name__=="__main__":
    tower = TowerOfHanoi(5)
    print(tower.towers)
    tower.move()
    print(tower.towers)
