from classes import Dog
from classes import Cat


puppy = Dog('Missy', 'white')
print('Name: ', end = '')
print(puppy.name)
puppy.run()
print(' ')


puppy2 = Dog('Buddy', 'black')
print('Name: ', end = '')
print(puppy2.name)
puppy2.run()
print(' ')

kitty = Cat('Bluebell', 'orange', 'shorthair')
print('Name: ', end = '')
print(kitty.name)
print('Colour:', end = '')
print(kitty.colour)
print('Breed: ', end = '')
print(kitty.breed)
print('Say hello! : ', end = '')
kitty.sound()
print(' ')

kitty2 = Cat('Stinky', 'brown', 'tabby')
print('Name: ', end = '')
print(kitty2.name)
print('Colour:', end = '')
print(kitty2.colour)
print('Breed: ', end = '')
print(kitty2.breed)
print('Say hello! : ', end = '')
kitty2.sound()
print(' ')

kitty3 = Cat('Mischief', 'black', 'bombay')
print('Name: ', end = '')
print(kitty3.name)
print('Colour:', end = '')
print(kitty3.colour)
print('Breed: ', end = '')
print(kitty3.breed)
print('Say hello! : ', end = '')
kitty3.sound()