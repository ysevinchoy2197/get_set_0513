# 9-masala:
class Game:
    def __init__(self, title, level):
        self.title = title
        self.__level = level

    def get_level(self):
        return self.__level

    def set_level(self, new_level):
        self.__level = new_level


g1 = Game('Minecraft', 10)
print(g1.title)
print(g1.get_level())
g1.set_level(20)
print(g1.get_level())
