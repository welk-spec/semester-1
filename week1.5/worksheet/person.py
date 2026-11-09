# Worksheet 1.5: Person class

from datetime import date


class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name: str, birth: date):
        """
        Creates a person, with given name and date of birth.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if name == "":
            raise ValueError("Name must not be empty")
        if not isinstance(birth, date):
            raise TypeError("Birth must be a date object")
        self.name = name
        self.birth = birth

    def initials(self):
        """
        Returns the initials of the person.
        """
        initials = ""
        for part in self.name.split():
            initials += part[0].upper()
        return initials

    def is_birthday(self):
        """
        Returns True if today is the person's birthday, False otherwise.
        """
        today = date.today()
        return today.month == self.birth.month and today.day == self.birth.day

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
