
class Plant:
    def __init__(self, name: str, height: int, Age: int):
        self.name = name.capitalize()
        self.height = height
        self.Age = Age
        self.new_height = 0
        self.new_age = 0

    def __str__(self):
        return f"Created: {self.name} ({self.height}cm, {self.Age} days)"

    def get_info(self):
        print("=== Day 1 ===")
        print(f"{self.name}: {self.height}cm,", end='')
        print(f" {self.Age} days old")
        print(f"=== Day {self.new_age + 1} ===")
        print(f"{self.name}: {self.height + self.new_height}cm,", end='')
        print(f" {self.Age + self.new_age} days old")
        print(f"Growth this week: +{self.new_age}cm")

    def grow(self):
        self.new_height += 1

    def age(self):
        self.new_age += 1


class PlantFactory:
    def __init__(self):
        self.plants = []

    def create_plant(self, name, height, age):
        self.plants.append(Plant(name, height, age))

    def display_plants(self):
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
