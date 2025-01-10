from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass
    
class Cachorro(Animal):
    def falar(self):
        return 'auau'
    
class Gato(Animal):
    def __init__(self, patas):
        self.patas = patas
    def falar(self):
        return 'miau'
    
gato = Gato(patas=4)
cachorro = Cachorro()
animais = [gato, cachorro]

for animal in animais:
    if isinstance(animal, Animal):
        if hasattr(animal, 'patas'):
            print(f'{type(animal).__name__} possui {animal.patas} patas')
        print(f'O {type(animal).__name__} fala: {animal.falar()}')
