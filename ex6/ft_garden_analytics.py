
class Plant:
    """Base class for all plants."""
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
    
    def get_name(self) -> str:
        return self._name

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

    def get_height(self) -> int:
        return self._height + self._new_height

    def get_age(self) -> int:
        return self._Age + self._new_age

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height

    def set_age(self, age: int):
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


class FloweringPlant(Plant):
    """Plants that produce flowers."""
    def __init__(self, name: str, height: int, age: int, flower_color: str, blooming = True):
        super().__init__(name, height, age)
        self.flower_color = flower_color
        self._blooming = blooming

    def grow(self):
        super().grow()
    
    def get_color(self) -> str:
        return self.flower_color

    def get_blomming(self) -> bool:
        return self._blooming
        # print(f"{self.get_name()} is blooming: {self.blooming}")


class PrizeFlower(FloweringPlant):
    """Flowering plants that can earn prize points."""
    def __init__(self, name: str, height: int, age: int, flower_color: str, blooming = True, prize_points = 0):
        super().__init__(name, height, age, flower_color, blooming)
        self._prize_points = prize_points

    def grow(self):
        super().grow()
        # print(f"{self.get_name()} Prize points: {self._prize_points}")
    
    def get_prize_points(self) -> int:
        return self._prize_points


class GardenManager:
    def __init__(self, gardener_name: str):
        self._gardener_name = gardener_name
        self._plants = []
        self.stats = self.GardenStats(self)

    class GardenStats:
        def __init__(self, manager):
            self.manager = manager
        
        def total_growth(self) -> int:
            total = 0
            for plant in self.manager.get_plants():
                total += plant.get_height()
            return total
        
        def plant_counts(self) -> tuple[int, int, int, int, int]:
            flowers = 0
            trees = 0
            vegetables = 0
            flowering_plant = 0
            prize_flower = 0


            for plant in self.manager.get_plants():
                if isinstance(plant, Flower):
                    flowers += 1
                elif isinstance(plant, Tree):
                    trees += 1
                elif isinstance(plant, FloweringPlant):
                    flowering_plant += 1
                elif isinstance(plant, PrizeFlower):
                    prize_flower += 1
                elif isinstance(plant, Vegetable):
                    vegetables += 1
            return flowers, trees, vegetables, flowering_plant, prize_flower
        
        def validate_heights(self, max_height=500) -> bool:
            """Utility to check if all plants are under max_height"""
            for p in self.manager.get_plants():
                if p.get_height() > max_height:
                    return False
            return True
    def get_gardener_name(self) -> str:
        return self._gardener_name
    
    def get_plants(self) -> list[Plant]:
        return self._plants

    def add_plant(self, plant) -> None:
        self._plants.append(plant)
        print(f"Added {plant.get_name()} to {self._gardener_name}'s garden")

    def help_plants_grow(self):
        print(f"{self._gardener_name} is helping all plants grow...")
        for plant in self._plants:
            plant.grow()
            print(f"{plant.get_name()} grew 1cm")




# Demo usage
if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    # self, name: str, height: int, age: int, trunk_diameter: int
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    # Adding plants
    alice_garden.add_plant(Plant("Oak Tree", 100, 23))
    alice_garden.add_plant(FloweringPlant("Rose", 25, 34, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, 12, "yellow", True, 10))
    
    bob_garden.add_plant(Plant("Maple", 40, 24))
    bob_garden.add_plant(Flower("Tulip", 30, 23, "pink"))

    # Grow plants
    alice_garden.help_plants_grow()

    # Garden report
    print(f"=== {alice_garden.get_gardener_name()}'s Garden Report ===")
    for plant in alice_garden.get_plants():
        desc = f"- {plant.get_name()}: {plant.get_height()}cm"
        if isinstance(plant, FloweringPlant):
            desc += f", {plant.get_color()} flowers (blooming: {plant.get_blomming()})"
        if isinstance(plant, PrizeFlower):
            desc += f", Prize points: {plant.get_prize_points()}"
        print(desc)

    total_plants = len(alice_garden.get_plants())
    total_growth = alice_garden.stats.total_growth()
    regular, flowering, prize = alice_garden.stats.plant_counts()
    height_valid = alice_garden.stats.validate_heights()

    print(f"Plants added: {total_plants}, Total growth: {total_growth}cm")
    print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")
    print(f"Height validation test: {height_valid}")

    # Garden network scores
    # scores = GardenManager.create_garden_network(alice_garden, bob_garden)
    # print(f"Garden scores - {', '.join(f'{k}: {v}' for k,v in scores.items())}")
    # print(f"Total gardens managed: {GardenManager.total_gardens}")
    
    # Utility function
    # GardenManager.utility_message()