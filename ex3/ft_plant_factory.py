
class Plant:
    """A class representing a plant with information."""

    def __init__(self, name: str, height: int, Age: int):
        self.name = name.capitalize()
        self.height = height
        self.Age = Age
        self.new_height = 0
        self.new_age = 0

    def __str__(self):
        """ return string about plant info """
        return f"Created: {self.name} ({self.height}cm, {self.Age} days)"

    def get_info(self):
        """ print plant info """
        print("=== Day 1 ===")
        print(f"{self.name}: {self.height}cm,", end='')
        print(f" {self.Age} days old")
        print(f"=== Day {self.new_age + 1} ===")
        print(f"{self.name}: {self.height + self.new_height}cm,", end='')
        print(f" {self.Age + self.new_age} days old")
        print(f"Growth this week: +{self.new_age}cm")

    def grow(self):
        """make plant grow with one cm"""
        self.new_height += 1

    def age(self):
        """make plant grow up one day"""
        self.new_age += 1


class PlantFactory:
    """A class representing a plantfactory for plants."""
    def __init__(self):
        self.plants = []

    def create_plant(self, name, height, age):
        """ create plant and add it to array of plants. """
        self.plants.append(Plant(name, height, age))

    def display_plants(self):
        """ print all plants info in plants array. """
        print("=== 🌱 Plant Factory Output 🌱 ===")
        for plant in self.plants:
            print(plant)


if __name__ == "__main__":
    factory = PlantFactory()
    factory.create_plant("Rose", 30, 1)
    factory.create_plant("Oak", 150, 10)
    factory.create_plant("Cactus", 25, 3)
    factory.create_plant("Tulip", 20, 1)
    factory.create_plant("Sunflower", 180, 2)
    factory.display_plants()
