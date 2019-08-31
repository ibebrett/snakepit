x = 1
y = 'hello'

class Orc:
    def __init__(self):
        self.hp = 1.0
        self.name = 'Gak'

ork = Orc()

a_cool_string = f'using f strings is fun, {x} and {y}'
not_cool_string = 'using f strings is fun, {x} and {y}'
coolest_string = f'A sweet orc called {ork.name} with hp {ork.hp}'

# NOTE how the f string actually uses the values of x and y.
print(a_cool_string)
print(not_cool_string)
print(coolest_string)
