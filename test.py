from random import choice


class Person:
    def __init__(self, name):
        self.greetings = 'Hello {name}'
        self.name = name

    def __str__(self):
        return self.make_greetings()

    def make_greetings(self):
        return self.greetings.format(name=self.name)


def main():
    people = [
        # Person('Bob'),
        # Person('Tom'),
        Person('Jim')
        # dict(name="Bob")
    ]
    person = choice(people)
    print(person)


if __name__ == '__main__':
    main()
