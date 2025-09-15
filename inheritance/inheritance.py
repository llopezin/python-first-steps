class Parent():
    _blood_type = 'A'

    @classmethod
    def change_blood_type(cls, new_type):
        cls._blood_type = new_type

    @classmethod
    def get_blood_type(cls):
        return cls._blood_type   

    def __init__(self, name, age):
        self._name = name
        self._age = age


class Child(Parent):
    def __init__(self, name, age, parent_name=None):
        self.parent_name = parent_name
        super().__init__(name, age)

def main():
    my_child = Child('child', 2)
    print(my_child.get_blood_type())
    Parent.change_blood_type('AB')
    print(my_child.get_blood_type())


if __name__ == "__main__":
    main()