class car:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print(self.name)

obj = car("WolksVagen")
obj.display_name()