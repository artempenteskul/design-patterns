import copy


# Thats just an object with reference for the example
class SelfReferencingEntity:
    def __init__(self) -> None:
        self.parent = None

    def set_parent(self, parent) -> None:
        self.parent = parent


# Python provides its own interface of Prototype via "copy.copy" and "copy.deepcopy" functions.
# And any class that wants to implement custom implementations have override '__copy__' and '__deepcopy__' member functions.
class SomeComponent:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref) -> None:
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    # Creates a shallow copy. This method will be called whenever someone calls 'copy.copy' with this object and the returned value is new shallow copy.
    def __copy__(self):
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)

        return new

    # Creates a deep copy. This method will be called whenever someone calls 'copy.deepcopy' with this object and the returned value is new deep copy.
    # Memo parameter is the dictionary that is used by the 'deepcopy' library to prevent infinite recursive copies in instances of circular references.
    # Pass it to all the 'deepcopy' calls you make in the '__deepcopy__' implementation to prevent infinite recursions.
    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}

        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo=memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo=memo)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__ = copy.deepcopy(self.__dict__, memo=memo)

        return new


if __name__ == '__main__':
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    # Making shallow copy
    print('=== Tests with shallow copy of the object ===')
    shallow_copied_component = copy.copy(component)

    # Lets add new object to the shallow copy some_list_of_objects property.
    shallow_copied_component.some_list_of_objects.append('shallow copy') 
    if component.some_list_of_objects[-1] == 'shallow copy':
        print('Adding elements to shallow copy some_list_of_objects adds it to component some_list_of_objects.')
    else:
        print('Adding elements to shallow copy some_list_objects does not add it to component some_list_of_objects.')

    # Lets change the set in the component list of objects.
    component.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print('Changing mutable objects in component some_list_of_objects changes shallow copy some_list_of_objects.')
    else:
        print('Changing mutable objects in the component some_list_of_objects does not change shallow copy some_list_of_objects.')

    # Making deep copy
    print()
    print('=== Tests with deep copy of the object ===')
    deep_copied_component = copy.deepcopy(component)

    # Lets add new object to the deep copy some_list_of_objects property.
    deep_copied_component.some_list_of_objects.append('deep copy')
    if component.some_list_of_objects[-1] == 'deep copy':
        print('Adding elements to deep copy some_list_objects adds it to the component some_list_of_objects.')
    else:
        print('Adding elements to deep copy some_list_objects does not add it to the component some_list_of_objects.')

    # Lets change the list in the component list of objects.
    component.some_list_of_objects[1].add(10)
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print('Changing mutable objects in component some_list_of_objects changes deep copy some_list_of_objects.')
    else:
        print('Changing mutable objects in the component some_list_of_objects does not change deep copy some_list_of_objects.')

    print()
    print(f"id(deep_copied_component.some_circular_ref.parent): {id(deep_copied_component.some_circular_ref.parent)}")
    print(f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): {id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}")

