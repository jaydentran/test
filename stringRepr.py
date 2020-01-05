class Human:

    def __init__(self, name = "somebody"):
        self.name = name

    def __repr__(self):
        return self.name

# dude = Human("Tri dep trai")
# print(dude)

tin = Human("Bach Beo")
tin = str(tin)
print(tin)
