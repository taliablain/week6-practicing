class Dog:
    name = ''
    colour = ''

    def __init__(self, str, colour):
        self.name = str
        self.colour = str

    def run(self):
        print("speedy!!")

#class Cat:
    #name = ''
    #colour = ''
    #breed = ''

    #def __init__(self, str, colour, breed):
        #self.name = str
        #self.colour = str
        #self.breed = str

    #def sound(self):
        #print("meow meow")

class Cat:
    def __init__(self, name, colour, breed):
        self.name = name
        self.colour = colour
        self.breed = breed

    def sound(self):
        print('meow meow')


