
class Plant:
    def __init__(self, name: str, height: int, Age: int):
        self._name = name.capitalize()
        self._height = 0
        self._Age = 0
        self._new_height = 0
        self._new_age = 0
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

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._Age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color
        self._bloom_status = False

    def bloom(self):
        self._bloom_status = True

    def set_color(self, color: str):
        self._color = color

    def get_bloom_status(self):
        return self._bloom_status

    def get_color(self):
        return self._color

    def print_info(self):
        print(f"{self._name} (Flower): {self._height}cm, {self._Age} days, ",
              end='')
        print(f"{self._color} color\n{self._name} ", end='')
        if self._bloom_status:
            print("is blooming beautifully!")
        else:
            print("is not blooming")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._produce_shade = 0

    def produce_shade(self):
        self._produce_shade += 1

    def set_trunk_diameter(self, value: int):
        self._trunk_diameter = value

    def get_produce_shade(self):
        return self._produce_shade

    def get_trunk_diameter(self):
        return self._trunk_diameter

    def print_info(self):
        print(f"{self._name} (Tree): {self._height}cm, {self._Age} days, ",
              end='')
        print(f"{self._trunk_diameter}cm diameter\n{self._name}", end='')
        print(f"provides {self._produce_shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def set_harvest_season(self, harvest_season: str):
        self._harvest_season = harvest_season

    def set_nutritional_value(self, value: str):
        self._nutritional_value = value

    def get_nutritional_value(self):
        return self._nutritional_value

    def get_harvest_season(self):
        return self._harvest_season

    def print_info(self):
        print(f"{self._name} (Vegetable): ", end='')
        print(f"{self._height}cm, {self._Age} days, ", end='')
        print(f"{self._harvest_season} harvest\n", end='')
        print(f"{self._name} is rich in {self._nutritional_value}")


if __name__ == "__main__":
    # Flowers
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")
    # Trees
    oak = Tree("Oak", 500, 1825, 50)
    maple = Tree("Maple", 300, 1095, 30)
    # Vegetables
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 40, 70, "autumn", "vitamin A")
    rose.bloom()
    oak.produce_shade()
    maple.produce_shade()
    maple.produce_shade()
    maple.produce_shade()
    # Display
    print("=== Garden Plant Types ===")
    rose.print_info()
    tulip.print_info()
    print("")
    oak.print_info()
    maple.print_info()
    print("")
    tomato.print_info()
    carrot.print_info()
