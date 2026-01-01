
class Plant:
    """Base class for all plants."""
    def __init__(self, name: str, height: int, Age: int) -> None:
        self._name = name.capitalize()
        self._height = 0
        self._Age = 0
        self._new_height = 0
        self._new_age = 0
        self.set_height(height)
        self.set_age(Age)

    def __str__(self) -> str:
        """ return string about plant info. """
        return f"Created: {self._name} ({self._height}cm, {self._Age} days)"

    def get_name(self) -> str:
        """return the name of the plant."""
        return self._name

    @classmethod
    def get_info(cls) -> None:
        """ print information of the plant."""
        print("=== Day 1 ===")
        print(f"{cls._name}: {cls._height}cm,", end='')
        print(f" {cls._Age} days old")
        print(f"=== Day {cls.new_age + 1} ===")
        print(f"{cls._name}: {cls._height + cls._new_height}cm,", end='')
        print(f" {cls._Age + cls._new_age} days old")
        print(f"Growth this week: +{cls._new_age}cm")

    def grow(self) -> None:
        """make the plant grow by one cm."""
        self._new_height += 1

    def age(self) -> None:
        """make the plant grow up by one day."""
        self._new_age += 1

    def get_height(self) -> int:
        """return the height of the plant."""
        return self._height + self._new_height

    def get_new_height(self) -> int:
        """return the new height of the plant."""
        return self._new_height

    def get_age(self) -> int:
        """return the age of the plant."""
        return self._Age + self._new_age

    def set_height(self, height: int) -> None:
        """set the height of the plant."""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        """set the age of the plant."""
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._Age = age


class FloweringPlant(Plant):
    """Plants that produce flowers."""
    def __init__(
            self, name: str, height: int, age: int,
            flower_color: str, blooming=True
            ) -> None:
        super().__init__(name, height, age)
        self.flower_color = flower_color
        self._blooming = blooming

    def grow(self) -> None:
        """make the flowering plant grow by one cm."""
        super().grow()

    def get_color(self) -> str:
        """return the color of the flowering plant"""
        return self.flower_color

    def get_blomming(self) -> bool:
        """get the blomming of the flowering plant."""
        return self._blooming
        # print(f"{self.get_name()} is blooming: {self.blooming}")


class PrizeFlower(FloweringPlant):
    """Flowering plants that can earn prize points."""
    def __init__(
            self, name: str, height: int, age: int, flower_color: str,
            blooming=True, prize_points=0
            ) -> None:
        super().__init__(name, height, age, flower_color, blooming)
        self._prize_points = prize_points

    def grow(self) -> None:
        """make the prieflower grow by one cm."""
        super().grow()

    def get_prize_points(self) -> int:
        """return the prize points."""
        return self._prize_points


class GardenManager:
    """Manages multiple gardens and analytics."""
    total_gardens = 0

    def __init__(self, gardener_name: str) -> None:
        self._gardener_name = gardener_name
        self._plants = []
        self.stats = self.GardenStats(self)
        GardenManager.total_gardens += 1

    class GardenStats:
        """a helper class for the garden manager."""
        def __init__(self, manager):
            self.manager = manager

        def total_growth(self) -> int:
            """return the total growth of plants."""
            total = 0
            for plant in self.manager.get_plants():
                total += plant.get_new_height()
            return total

        def plant_counts(self) -> tuple[int, int, int]:
            """return the plants count (regular and flowering and prize)."""
            regular, flowering, prize = 0, 0, 0
            for p in self.manager.get_plants():
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        def validate_heights(self, max_height=500) -> bool:
            """Utility to check if all plants are under max_height."""
            for p in self.manager.get_plants():
                if p.get_height() > max_height:
                    return False
            return True

    def get_gardener_name(self) -> str:
        """return the gardener name of this plant."""
        return self._gardener_name

    def get_plants(self) -> list[Plant]:
        """return the plants array."""
        return self._plants

    def add_plant(self, plant) -> None:
        """adding a plant to the plants array."""
        self._plants.append(plant)
        print(f"Added {plant.get_name()} to {self._gardener_name}'s garden")

    def help_plants_grow(self):
        """make all plants grow by one cm."""
        print(f"\n{self._gardener_name} is helping all plants grow...")
        for plant in self._plants:
            plant.grow()
            print(f"{plant.get_name()} grew 1cm")

    @staticmethod
    def create_garden_network(*managers):
        """Class-level method to report garden network scores."""
        scores = {}
        for m in managers:
            total = 0
            for plant in m.get_plants():
                if isinstance(plant, PrizeFlower):
                    total += 15
                    total += plant.get_height()
                elif isinstance(plant, FloweringPlant):
                    total += 15
                    total += plant.get_height()
                elif isinstance(plant, Plant):
                    total += 10
                    total += plant.get_height()
            scores[m.get_gardener_name()] = total
        return scores

    @staticmethod
    def utility_message():
        """utility message."""
        print("Garden Manager Utility Function: Organize your gardens wisely!")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")
    # Adding plants
    alice_garden.add_plant(Plant("Oak Tree", 100, 23))
    alice_garden.add_plant(FloweringPlant("Rose", 25, 34, "red"))
    alice_garden.add_plant(
        PrizeFlower("Sunflower", 50, 12, "yellow", True, 10)
        )
    bob_garden.add_plant(Plant("Maple", 15, 24))
    bob_garden.add_plant(FloweringPlant("Tulip", 17, 23, "pink"))
    bob_garden.add_plant(PrizeFlower("Sunflower", 20, 12, "blue", True, 10))
    # Grow plants
    alice_garden.help_plants_grow()
    # Garden report
    print(f"\n=== {alice_garden.get_gardener_name()}'s Garden Report ===")
    for plant in alice_garden.get_plants():
        desc = f"- {plant.get_name()}: {plant.get_height()}cm"
        if isinstance(plant, FloweringPlant):
            desc += f", {plant.get_color()} flowers "
            if plant.get_blomming():
                desc += "(blooming)"
            else:
                desc += "(not blooming)"
        if isinstance(plant, PrizeFlower):
            desc += f", Prize points: {plant.get_prize_points()}"
        print(desc)
    total_plants = len(alice_garden.get_plants())
    total_growth = alice_garden.stats.total_growth()
    regular, flowering, prize = alice_garden.stats.plant_counts()
    height_valid = alice_garden.stats.validate_heights()
    print(f"\nPlants added: {total_plants}, Total growth: {total_growth}cm")
    print(f"Plant types: {regular} regular, ", end='')
    print(f"{flowering} flowering, {prize} prize flowers")
    print(f"\nHeight validation test: {height_valid}")
    # Garden network scores
    scores = GardenManager.create_garden_network(alice_garden, bob_garden)
    print("Garden scores - ", end='')
    for key, value in scores.items():
        print(f",{key}: {value} ", end='')
    print("")
    print(f"Total gardens managed: {GardenManager.total_gardens}")
    # Utility function
    GardenManager.utility_message()
