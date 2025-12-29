
class Plant:
    def __init__(self, name: str, height: int, Age: int):
        self._name = name.capitalize()
        self._height = 0
        self._Age = 0
        self._new_height = 0
        self._new_age = 0
        print("Plant created:", self._name)
        self.set_height(height)
        self.set_age(Age)

    def __str__(self):
        return f"Created: {self._name} ({self._height}cm, {self._Age} days)"

    def get_info(self):
        print("=== Day 1 ===")
        print(f"{self._name}: {self._height}cm,", end='')
        print(f" {self._Age} days old")
        print(f"=== Day {self.new_age + 1} ===")
        print(f"{self._name}: {self._height + self._new_height}cm,", end='')
        print(f" {self._Age + self._new_age} days old")
        print(f"Growth this week: +{self._new_age}cm")

    def grow(self):
        self._new_height += 1

    def age(self):
        self._new_age += 1

    def get_height(self):
        return self._height + self._new_height

    def get_age(self):
        return self._Age + self._new_age

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._Age = age
            print(f"Age updated: {age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 25, 30)
    plant.set_height(-5)
    print(plant)
