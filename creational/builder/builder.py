from typing import Any
from abc import ABC, abstractmethod


# It makes sense to use the Builder pattern only when your products are quite complex and require extensive configuration.
class Product1:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f'Product parts: {", ".join(self.parts)}', end='')



# The Builder interface specifies methods for creating the different parts of the Product objects.
class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def add_part_a(self) -> None:
        pass

    @abstractmethod
    def add_part_b(self) -> None:
        pass

    @abstractmethod
    def add_part_c(self) -> None:
        pass


# The Concrete Builder classese follow the Builder interface and provide specific implementations of the building steps.
# Your program may have several variations of Builders, implemented differently. 
class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1():
        product = self._product
        self.reset()
        return product

    def reset(self) -> None:
        self._product = Product1()

    def add_part_a(self) -> None:
        return self._product.add('Part A')

    def add_part_b(self) -> None:
        return self._product.add('Part B')

    def add_part_c(self) -> None:
        return self._product.add('Part C')


# The Director is only responsible for executing the building steps in a particular sequence.
# It is helpful when producing products according to a specific order or configuration. Strictly speaking, the Director class is optional, since the client can control Builders.
class Director:
    def __init__(self) -> None:
        self._builder = None

    @property 
    def builder(self) -> Builder:
        return self._builder

    # The Director works with any builder instance that the client code passes to it. 
    # This way, the client code may alter the final type of the newly assembled product.
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder


    # The Director can construct several product variations using the same building steps.
    def build_minimal_variable_product(self) -> None:
        self.builder.add_part_a()

    def build_fully_featured_product(self) -> None:
        self.builder.add_part_a()
        self.builder.add_part_b()
        self.builder.add_part_c()


# The clients code creates the builder object, passes it to the director and then initiates the construction process. The end result is retrieved from the builder object.
if __name__ == '__main__':
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print('Standard basic product')
    director.build_minimal_variable_product()
    builder.product.list_parts()

    print()

    print('Fully featured product')
    director.build_fully_featured_product()
    builder.product.list_parts()

    print()

# Remember, the Builder pattern can be used without the Director class (client code could operate Builder directly)
