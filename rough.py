class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal:
    def give_birth(self):
        print("Mammal gives birth")

class Dog(Animal, Mammal):
    def bark(self):
        print("Dog barks")

# Creating an instance of the Dog class
dog = Dog()

# Calling methods from the inherited classes
dog.speak()        # Output: Animal speaks
dog.give_birth()   # Output: Mammal gives birth
dog.bark()         # Output: Dog barks
