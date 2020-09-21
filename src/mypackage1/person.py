"""
This is a docstring for the person module.
"""


global_var = 'pigimaru'


def global_function() -> None:
    """This is docstring."""
    pass


def global_function2() -> None:
    pass


class Person:
    """Person class.
    """
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> None:
        """With docstring"""
        print(f"Hi! I'm {self.name}, {self.age} years old.")

    def without_docstring(self) -> None:
        pass

    def _private_method_with_docstring(self) -> None:
        """Should not be in the doc by default."""
        pass

    @staticmethod
    def add(a: int, b: int) -> int:
        """With docstring"""
        return a + b

    @staticmethod
    def subtract(a: int, b: int) -> int:
        return a - b


class Man(Person):
    """You have to set 'show-inheritance' to show the base class int the doc.

    Examples:
        ex1. A man can greet.

        >>> man = Man('pigimaru', 47)
        >>> man.greet()

        ex2. A man can kill another person.

        >>> man = Man('pigimaru', 47)
        >>> other = Man('foo', 23)
        >>> man.kill(other)
        >>> # See stdout.

    Todo:
        * For module TODOs
        * You have to also use ``sphinx.ext.todo`` extension
    """
    def __init__(self, name: str, age: int) -> None:
        """This is init docstring."""
        super().__init__(name, age)

    def work(self) -> None:
        """For my family."""
        pass

    def kill(self, target: Person) -> None:
        """Summary description.
        Main description.

        Args:
            target: The target person he's gonna kill

        Returns:
            None. This is just a print statement.
        """
        print(f"You are dead, {target.name}")
