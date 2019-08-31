from datetime import datetime


class Battle:
    def __enter__(self):
        print("The battle is starting")

    def __exit__(self, *args):
        print("The battle is ending")


class Timer:
    def __enter__(self):
        self.start_time = datetime.now()

    def __exit__(self, *args):
        total_time = datetime.now() - self.start_time
        print(f"Timer took {total_time}")
        

battle = Battle()

with battle:
    print("woohoo attack")


with Timer():
    for i in range(2, 10000):
        for j in range(2, i-1):
            pass
