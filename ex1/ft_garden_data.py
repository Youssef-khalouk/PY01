
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def desplay(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant1.desplay()
    plant2 = Plant("Sunflower", 80, 45)
    plant2.desplay()
    plant3 = Plant("Cactus", 15, 120)
    plant3.desplay()
