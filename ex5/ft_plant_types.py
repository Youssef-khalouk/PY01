
class Plant:
    """A class representing a plant with information."""
    def __init__(self, name: str, height: int, Age: int):
        self._name = name.capitalize()
        self._height = 0
        self._Age = 0
        self._new_height = 0
        self._new_age = 0
        self.set_height(height)
        self.set_age(Age)

    def __str__(self):
        """ return string about plant info. """
        return f"Created: {self._name} ({self._height}cm, {self._Age} days)"

    def get_info(self):
        """ print plant info. """
        print("=== Day 1 ===")
        print(f"{self._name}: {self._height}cm,", end='')
        print(f" {self._Age} days old")
        print(f"=== Day {self.new_age + 1} ===")
        print(f"{self._name}: {self._height + self._new_height}cm,", end='')
        print(f" {self._Age + self._new_age} days old")
        print(f"Growth this week: +{self._new_age}cm")

    def grow(self):
        """make plant grow with one cm."""
        self._new_height += 1

    def age(self):
        """make plant grow up one day."""
        self._new_age += 1

    def get_height(self):
        """get the height of the plant."""
        return self._height + self._new_height

    def get_age(self):
        """get the age of the plant."""
        return self._Age + self._new_age

    def set_height(self, height):
        """set the height to the plant."""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height

    def set_age(self, age):
        """set the age to the plant."""
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._Age = age


class Flower(Plant):
    """ A class representing a Flower plant with information. """
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color
        self._bloom_status = False

    def bloom(self):
        """blooming the flower plant."""
        self._bloom_status = True

    def set_color(self, color: str):
        """set the color of flower plant."""
        self._color = color

    def get_bloom_status(self):
        """ get the plooming status of the flower plant."""
        return self._bloom_status

    def get_color(self):
        """get the color of the flower"""
        return self._color

    def print_info(self):
        """print info of flower plant."""
        print(f"{self._name} (Flower): {self._height}cm, {self._Age} days, ",
              end='')
        print(f"{self._color} color\n{self._name} ", end='')
        if self._bloom_status:
            print("is blooming beautifully!")
        else:
            print("is not blooming")


class Tree(Plant):
    """ A class representing a Tree plant with information. """
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._produce_shade = 0

    def produce_shade(self):
        """produce shade of the tree plant."""
        self._produce_shade += 1

    def set_trunk_diameter(self, value: int):
        """set truck diameter to the tree plant."""
        self._trunk_diameter = value

    def get_produce_shade(self):
        """get the produce shade of the tree."""
        return self._produce_shade

    def get_trunk_diameter(self):
        """get trunk dimeter of the tree plant."""
        return self._trunk_diameter

    def print_info(self):
        """print the info of the tree plant."""
        print(f"{self._name} (Tree): {self._height}cm, {self._Age} days, ",
              end='')
        print(f"{self._trunk_diameter}cm diameter\n{self._name}", end='')
        print(f"provides {self._produce_shade} square meters of shade")


class Vegetable(Plant):
    """ A class representing a vegetable plant with information. """
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def set_harvest_season(self, harvest_season: str):
        """set the harvest season to the vegetable plant."""
        self._harvest_season = harvest_season

    def set_nutritional_value(self, value: str):
        """set the ntritional value to the vegetable plant."""
        self._nutritional_value = value

    def get_nutritional_value(self):
        """get the nutritional value of the vegetable plant."""
        return self._nutritional_value

    def get_harvest_season(self):
        """get the harvest season of the vegetable plant."""
        return self._harvest_season

    def print_info(self):
        """print information of the vegetable plant."""
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
