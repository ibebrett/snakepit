class Battle:
    def __enter__(self):
        print("The battle is starting")

    def __exit__(self, *args):
        print("The battle is ending")

battle = Battle()

with battle:
    print("woohoo attack")
