
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age
        self.start_height = 0;

    def get_info(self):
        print(f"=== Day {self.days} ===")
        print(f"{self.name}: {self.height}cm,", end = "") 
        print(f"{self.age + self.days} days old")
        print(f"Growth this week: +{self.days}cm")        

    def grow(self):
        self.height += 1

    def age(self):
        self.age += 1;

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant1.age()


$> python3 ft_plant_growth.py
=== Day 1 ===
Rose: 25cm, 30 days old
=== Day 7 ===
Rose: 31cm, 36 days old
Growth this week: +6cm