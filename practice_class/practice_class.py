class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def speak(self):
        return f'I am {self.name} and I have {self.hp} hp'

mike = Character('mike', 10)
sally = Character('sally', 12)

print(sally.speak())
print(sally.name)
