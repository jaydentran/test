# __name

class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "Hi!"
        self.__msg = "I like turtles!"
        self.__lol = "HAHAHAHA"

p = Person()

print(p.name)
print(p._secret)
print(p._Person__msg)
print(p._Person__lol)

