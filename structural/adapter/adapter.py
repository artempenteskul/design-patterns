class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """
    def request(self) -> str:
        return 'Target: The default target behaviour.'

    
class Adaptee:
    """
    The Adaptee contains some useful behaviour, but its interface is incompatible with existing clients code.
    The Adaptee needs some adaptation before clients code can use it.
    """
    def specific_request(self) -> str:
        return '.eetpadA eht fo roivaheb laicepS'


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's interface via multiple inheritance.
    """
    def request(self) -> str:
        return f'Adapter: (TRANSLATED) {self.specific_request()[::-1]}'


def clients_code(target: Target) -> None:
    """
    The clients code supports all classes that follows the Target's interface.
    """
    print(target.request(), end='')


if __name__ == '__main__':
    print('Client: I can work just fine with the Target objects.')
    target = Target()
    clients_code(target=target)
    print('\n')

    adaptee = Adaptee()
    print('Client: Adaptee class has weird interface, I cannot work with it.')
    print(f'Adaptee: {adaptee.specific_request()}')
    print('\n')

    print('Client: But I can work with it using Adapter class.')
    adapter = Adapter()
    clients_code(adapter)
    print('\n')
