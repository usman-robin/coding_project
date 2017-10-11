
class Person(object):
    def __init__(self, name=None, age=None):

        self.name = name
        self.age = age

    def __str__(self):
        print("Name: {} Age: {}".format(self.name, self.age))

    def walk(self):
        print ("walking")


class Employee(Person):
    def __init__(self, name=None, age=None, staffnum=None):
        super(Employee, self).__init__(name=name, age=age)
        self.staffnum = staffnum

    # Completely overriding
    def __str__(self):
        print("Name: {} Age: {} StaffNum: {}".format(self.name, self.age, self.staffnum))

    # Partial overriding
    def walk(self):
        print ("Employee is")
        super(Employee, self).walk()


if __name__ == '__main__':
    p = Person(name="John", age=23)

    p.__str__()

    e = Employee(name="Ana", age=18, staffnum=2)
    e.__str__()
    e.walk()
