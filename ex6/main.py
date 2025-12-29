# ft_garden_analytics.py

class Plant:
    """Base class for all plants."""
    def __init__(self, name, height=0):
        self.name = name
        self.height = height

    def grow(self, cm=1):
        self.height += cm
        print(f"{self.name} grew {cm}cm")


class FloweringPlant(Plant):
    """Plants that produce flowers."""
    def __init__(self, name, height=0, flower_color="unknown", blooming=True):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.blooming = blooming

    def grow(self, cm=1):
        super().grow(cm)
        print(f"{self.name} is blooming: {self.blooming}")


class PrizeFlower(FloweringPlant):
    """Flowering plants that can earn prize points."""
    def __init__(self, name, height=0, flower_color="unknown", blooming=True, prize_points=0):
        super().__init__(name, height, flower_color, blooming)
        self.prize_points = prize_points

    def grow(self, cm=1):
        super().grow(cm)
        print(f"{self.name} Prize points: {self.prize_points}")


class GardenManager:
    """Manages multiple gardens and analytics."""
    total_gardens = 0

    def __init__(self, gardener_name):
        self.gardener_name = gardener_name
        self.plants = []
        self.stats = self.GardenStats(self)
        GardenManager.total_gardens += 1

    # Nested helper class for garden statistics
    class GardenStats:
        def __init__(self, manager):
            self.manager = manager

        def total_growth(self):
            return sum(p.height for p in self.manager.plants)

        def plant_counts(self):
            regular, flowering, prize = 0, 0, 0
            for p in self.manager.plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        def validate_heights(self, max_height=500):
            """Utility to check if all plants are under max_height"""
            return all(p.height <= max_height for p in self.manager.plants)

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.gardener_name}'s garden")

    def help_plants_grow(self):
        print(f"{self.gardener_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    @classmethod
    def create_garden_network(cls, *managers):
        """Class-level method to report garden network scores."""
        scores = {m.gardener_name: m.stats.total_growth() * 2 for m in managers}
        return scores

    @staticmethod
    def utility_message():
        print("Garden Manager Utility Function: Organize your gardens wisely!")


# Demo usage
if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    # Adding plants
    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", True, 10))
    
    bob_garden.add_plant(Plant("Maple", 40))
    bob_garden.add_plant(FloweringPlant("Tulip", 30, "pink"))

    # Grow plants
    alice_garden.help_plants_grow()

    # Garden report
    print(f"=== {alice_garden.gardener_name}'s Garden Report ===")
    for plant in alice_garden.plants:
        desc = f"- {plant.name}: {plant.height}cm"
        if isinstance(plant, FloweringPlant):
            desc += f", {plant.flower_color} flowers (blooming: {plant.blooming})"
        if isinstance(plant, PrizeFlower):
            desc += f", Prize points: {plant.prize_points}"
        print(desc)

    total_plants = len(alice_garden.plants)
    total_growth = alice_garden.stats.total_growth()
    regular, flowering, prize = alice_garden.stats.plant_counts()
    height_valid = alice_garden.stats.validate_heights()

    print(f"Plants added: {total_plants}, Total growth: {total_growth}cm")
    print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")
    print(f"Height validation test: {height_valid}")

    # Garden network scores
    scores = GardenManager.create_garden_network(alice_garden, bob_garden)
    print(f"Garden scores - {', '.join(f'{k}: {v}' for k,v in scores.items())}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")
    
    # Utility function
    GardenManager.utility_message()
