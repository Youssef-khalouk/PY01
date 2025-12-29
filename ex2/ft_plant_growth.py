
class Plant:
    def __init__(self, name: str, height: int, Age: int):
        self.name = name.capitalize()
        self.height = height
        self.Age = Age
        self.new_height = 0
        self.new_age = 0

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


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant1.age()
    plant1.grow()
    plant1.age()
    plant1.grow()
    plant1.age()
    plant1.grow()
    plant1.age()
    plant1.grow()
    plant1.age()
    plant1.grow()
    plant1.age()
    plant1.grow()
    plant1.get_info()
