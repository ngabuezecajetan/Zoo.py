# программа для управления зоопарком

class Animal:
    def __init__(self, species, name, age, weight):
        self.species = species
        self.name = name
        self.age = age
        self.weight = weight

    def feed(self, food):
        print(f"{self.name} is eating {food}...")

    def sleep(self):
        print(f"{self.name} is sleeping...")

class Zoo:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.animals = []

    def add_animal(self, animal):
        if len(self.animals) < self.capacity:
            self.animals.append(animal)
        else:
            print("Zoo is full, cannot add more animals.")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
        else:
            print("Animal not found in zoo.")

    def feed_animals(self, food):
        print(f"Feeding all animals in {self.name} with {food}...")
