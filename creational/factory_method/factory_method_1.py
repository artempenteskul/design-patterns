from abc import ABC, abstractmethod


""" The Product interface declares the operations that all concrete products must implement. """

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


""" Concrete Products provide various implementations of the Product interface. """

class Product1(Product):
    def operation(self) -> str:
        return 'Result of the Product2'


class Product2(Product):
    def operation(self) -> str:
        return 'Result of the Product2'



""" The Creator class declares the factory method that is supposed to return an object of a Product class. The Creator's subclasses usually provide the implementation of this method. """
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


""" Concrete Creators subclasses override the factory method in order to change the resulting product's type. """

class Creator1(Creator):
    def factory_method(self) -> Product:
        return Product1()


class Creator2(Creator):
    def factory_method(self) -> Product:
        return Product2()


#############################

def client_code(creator: Creator) -> None:
    print('This code is not aware of the actual Creator class, but still works!')
    print(f'Operation: {creator.some_operation()}')

if __name__ == '__main__':
    print('App: Launched with the ConcreteCreator1.')
    client_code(Creator1())
    print()

    print('App: Launched with the ConcreteCreator2.')
    client_code(Creator2())
    print()
