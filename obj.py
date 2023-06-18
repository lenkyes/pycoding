


class Animal:
    def __init__(self, name):
        self.name = name

    def __copy__(self):
        return type(self)(self.name)

    def __eq__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self.name == other.name

    def __repr__(self):
        return f"{type(self).__name__}({self.name!r})"


class Dog(Animal):
    pass


def normal_usage():
    a = Animal("lenk")
    print(a)

normal_usage()