# The Singleton class can be implemented in different ways in Python.
# Some possible methods include: base class, decorator, metaclass. In this example, metaclass version is used.
class SingletonMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]


# In this Singleton class we can implement the bussiness logic. Its metaclass follows the pattern and returns always same object.
class Singleton(metaclass=SingletonMeta):
    def bussiness_logic(self):
        print('Bussiness logic here.')


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print('Singleton works, always returns the same instance.')
    else:
        print('Seems that Singleton does not work.')
        