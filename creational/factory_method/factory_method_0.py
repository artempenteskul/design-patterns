import random

from abc import ABC, abstractmethod


# interface for the different variations (all variations should inherit one interface)
class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def on_click(self) -> None:
        pass


# first variation of Button interface
class WindowsButton(Button):
    def render(self) -> None:
        print('Windows rendering')

    def on_click(self) -> None:
        print('Windows on_click')


# second variation of Button interface
class HTMLButton(Button):
    def render(self) -> None:
        print('HTML rendering')

    def on_click(self) -> None:
        print('HTML on_click')


# basic class with factory_method (this method will be overwritten in the subclasses)
class Dialog:
    def render(self) -> None:
        button = self.create_button()
        button.on_click()
        button.render()

    @abstractmethod
    def create_button(self) -> Button:
        pass


# first subclass which overwrites factory_method (returns one of the variants of Button interface)
class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()


# second subclass which overwrites factory_method (returns one of the variants of Button interface)
class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HTMLButton()


# client code (application code is not dependent on the specific Button or Dialog, we could easily add new one)
class Application:
    def __init__(self, config=random.choice(['Windows', 'Web'])) -> None:
        if config == 'Windows':
            self.dialog = WindowsDialog()
        elif config == 'Web':
            self.dialog =  WebDialog()
        else:
            raise Exception('Error! Unknown config.')
    

if __name__ == '__main__':
    application = Application()
    application.dialog.render()
 