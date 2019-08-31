class Sword:
    def deal_damage(self):
        return 10

class Dagger:
    def deal_damage(self):
        return 5

class Character:
    def __init__(self, name, hp, weapons):
        self.name = name
        self.hp = hp
        self.weapons = weapons

    def speak(self):
        return f'I am {self.name} and I have {self.hp} hp'
    
    def wave(self):
        return f'{self.name} waves hello.'

    def attack(self):
        total_damage = 0
        for weapon in self.weapons:
            total_damage += weapon.deal_damage()

        return total_damage

mike = Character('mike', 10, [Sword()])
sally = Character('sally', 12, [Sword(), Dagger()])

print(sally.speak())
print(sally.name)
print(sally.wave())

sally_damage = sally.attack()
print(f'Sally attacks with {sally_damage}')
