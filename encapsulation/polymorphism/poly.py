#polymorphism-multiple forms
from abc import ABC,abstractmethod
class Animal (ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "woof"
class cat(Animal):
    def make_sound(self):
        return "meaow"
cat1 = cat(

)
print(cat1.make_sound())