from abc import ABC, abstractmethod


# Each distinct product of a product family should have base interface. All variants of the product must implement this interface.
class Button(ABC):
    def paint(self) -> str:
        pass


# Concrete products are created by corresponding concrete factories.
class WinButton(Button):
    def paint(self) -> str:
        return 'Windows Button'


# Concrete products are created by corresponding concrete factories.
class MacButton(Button):
    def paint(self) -> str:
        return 'Mac Button'


# That's the interface for another product. All variants must implement this interface. 
class CheckBox(ABC): 
    def paint(self) -> str:
        pass


# Concrete product from the CheckBox interface 
class WinCheckBox(CheckBox):
    def paint(self) -> str:
        return 'Windows CheckBox'


# Concrete product from the CheckBox interface
class MacCheckBox(CheckBox):
    def paint(self) -> str:
        return 'Mac CheckBox'

    
# The abstract factory declares the set of methods that return different abstract products. These products are called family and are related by a high-level theme or concept.
# Abstract factory knows about all sorts of the products.
class GUIFactory(ABC):
    def create_button(self) -> Button:
        pass

    def create_checkbox(self) -> CheckBox:
        pass


# Each factory knows only about its variation of objects and creates only those objects.
class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> CheckBox:
        return WinCheckBox()


# Each factory knows only about its variation of objects and creates only those objects.
class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> CheckBox:
        return MacCheckBox()
