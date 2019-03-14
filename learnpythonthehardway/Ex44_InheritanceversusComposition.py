class Parent(object):
    # Implicit Inheritance
    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):
    # Override Explicitly
    def override(self):
        print("CHILD override()")

    # Alter Before or After
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


class Other(object):
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicity()")

    def altered(self):
        print("OTHER altered()")


class Boy(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("BOY override()")

    def altered(self):
        print("BOY, BEFORE OTHER altered()")
        self.other.altered()
        print("BOY, AFTER OTHER altered()")


boy = Boy()
boy.implicit()
boy.override()
boy.altered()
