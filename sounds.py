#### Inheritance
"""
class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print(f"The animal {self.name} makes sound.")

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

class Animal:
    def __init__(self, name) -> None:
        self.name = name
        self.legs = '0 to 1000 legs'

    def make_sound(self):
        print(f"The animal makes sound.")

class Dog(Animal):
    def __init__(self, name, color) -> None:
        super().__init__(name) # calling the parent's __init__
        self.color = color

    def make_sound(self):
        print(f'The {self.color} dog {self.name} barks with {self.legs}')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('The Cat miauos')



class Animal:
    legs = '0-1000'
    def __init__(self, name) -> None:
        self.name = name
        self.legs = '0 to 1000 legs'

    def make_sound(self):
        print(f"The animal makes sound.")

class Mice(Animal):
    def __init__(self) -> None:
        self.name = 'Bla'
        
    def make_sound(self):
        print(self.legs)

dog = Dog('Fido', 'red')
dog.make_sound()
mice = Mice()
mice.make_sound()"""


import os
from playsound import playsound


# Get the directory path containing the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Specify the folder name
audio_folder = "audio_files"

# Get the paths of the MP3 files
mp3_file_dog = os.path.join(script_dir, audio_folder, 'dog_sound.mp3')
mp3_file_cat = os.path.join(script_dir, audio_folder, 'cat_sound.mp3')


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"The animal {self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        playsound(mp3_file_dog)
        print(f"The dog {self.name} barks.")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        playsound(mp3_file_cat)
        print(f"The cat {self.name} meows.")

# Create instances of Dog and Cat
dog = Dog('Fido')
#cat = Cat('Whiskers')

# Make the sounds of the animals
dog.make_sound()
#cat.make_sound()

