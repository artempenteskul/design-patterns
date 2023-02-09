import random

from abc import ABC, abstractmethod


# interface of the different types of products
class Button(ABC):
    def render(self):
        pass

    @abstractmethod
    def on_click(self):
        pass


# first type of the Button
class WindowsButton(Button):
    def render(self):
        print('rendering windows')

    def on_click(self):
        print('windows on click')


# second type of the Button
class HTMLButton(Button):
    def render(self):
        print('rendering html')

    def on_click(self):
        print('html on click')


# basic class with fabric method
class Dialog:
    def render(self):
        button = self.create_button()
        button.on_click()
        button.render()

    @abstractmethod
    def create_button(self) -> Button:
        pass


# first concrete fabric which overrides fabric method
class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()


# second concrete fabric which overrides fabric method
class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HTMLButton()


############################ 

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
 