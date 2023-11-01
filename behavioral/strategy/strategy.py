from abc import ABC, abstractmethod


class Context:
    """
    The Context defines the interface of interest to clients.
    """
    def __init__(self, strategy: 'Strategy') -> None:
        """
        Usually, the Context accepts a strategy through the constructor,
        but also provides a setter to change it at runtime.
        """
        self._strategy = strategy

    @property
    def strategy(self) -> 'Strategy':
        """
        The Context maintains a reference to one of the Strategy objects.
        The Context does not know the concrete class of the strategy.
        It should work with all strategies via the Strategy interface.
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: 'Strategy') -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        The Context delegates some work to the Strategy object instead of implementing multiple versions of the
        algorithm on its own.
        """
        print('Context: Sorting data using the strategy (not sure how it will do it).')
        result = self._strategy.do_algorithm(['a', 'b', 'c', 'd', 'e'])
        print(','.join(result))


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions of some algorithm.
    The Context uses this interface to call the algorithm defined by Concrete Strategies.
    """

    @abstractmethod
    def do_algorithm(self, data: list):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy interface.
The interface makes them interchangeable in the Context.
"""


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: list):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: list):
        return reversed(sorted(data))


if __name__ == '__main__':
    strategy_a = ConcreteStrategyA()
    strategy_b = ConcreteStrategyB()

    context = Context(strategy_a)
    context.do_some_business_logic()

    context.strategy = strategy_b

    context.do_some_business_logic()
