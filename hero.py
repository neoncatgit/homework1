class SuperHero:
    people = "people"

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def nameforhero(self):
        print(f"Имя героя {self.name}")

    def health_point(self):
        print(f"Здоровье героя {self.health_points * 2}")

    def __str__(self):
        return f"{self.nickname} {self.superpower} {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Брюс Уэйн", "Бэтмен", "Деньги", 100, "Не то, кем я являюсь, а то, что я делаю, определяет меня")
print(hero)
SuperHero.nameforhero(hero)
SuperHero.health_point(hero)
print(len(hero))