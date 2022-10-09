class Person:

    # Add the constructor method here
    # - It should take one argument, the name of the person
    # - The name argument should be stored in an attribute called "name"
    # - The default value "John" should be assigned to the name if no argument is passed

    def __init__(self, name="John"):
        self.name = name


def main():
    person_1 = Person("Bob")
    person_2 = Person()
    print(person_1.name)
    print(person_2.name)


if __name__ == "__main__":
    main()
