# class animalShelter:
#
#     def __init__(self, type=None):
#         self.dogQueue = []
#         self.catQueue = []
#         self.type = type
#
#     def enqueue(self, animal, arrivalTime, type):
#         if type == "dog":
#             self.dogQueue.insert(0, {animal: arrivalTime})
#         elif type == "cat":
#             self.catQueue.insert(0, {animal: arrivalTime})
#         else:
#             return("Sorry, animal shelter open only for cats and dogs for now! :()")
#
#     def dequeueAny(self):
#         if self.catQueue:
#             catTime = self.catQueue[len(self.catQueue)-1].values()
#         if self.dogQueue:
#             dogTime = self.dogQueue[len(self.dogQueue)-1].values()
#         if catTime < dogTime:
#             print(self.catQueue.pop().keys()[0])
#             return self.catQueue.pop().keys()[0]
#         else:
#             print(self.dogQueue.pop().keys()[0])
#             return self.dogQueue.pop().keys()[0]
#
#     def dequeueDog(self):
#         print(self.dogQueue.pop().keys()[0])
#         return self.dogQueue.pop().keys()[0]
#
#     def dequeueCat(self):
#         print(self.catQueue.pop().keys()[0])
#         return self.catQueue.pop().keys()[0]
#
#
# if __name__=="__main__":
#     shelter = animalShelter()
#     shelter.enqueue("corgi", 8, "dog")
#     shelter.enqueue("bender", 7, "dog")
#     shelter.enqueue("bitch", 2, "cat")
#     shelter.enqueue("bitchass", 11, "cat")
#     shelter.dequeueAny()
#     shelter.enqueue("bleep", 5, "dog")
#     shelter.dequeueDog()

class Animal(object):
    def __init__(self, animalName = None, animalType = None, next = None):
        self.animalName = animalName
        self.animalType = animalType
        self.next = next
        self.timestamp = 0

class AnimalShelter(object):
    def __init__(self):
        self.headCat = None
        self.headDog = None
        self.tailCat = None
        self.tailDog = None
        self.animalNumber = 0

    def enqueue(self, animalName, animalType):
        self.animalNumber += 1
        newAnimal = Animal(animalName, animalType)
        newAnimal.timestamp = self.animalNumber

        if animalType == "dog":
            if not self.headDog:
                self.headDog = newAnimal
            if self.tailDog:
                self.tailDog.next = newAnimal
            self.tailDog = newAnimal

        elif animalType == "cat"
