import sys


class Person(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print("create a object person, name is %s, weight is %d" %(self.name, self.weight))

    def eat(self):
        self.weight += 1
        print("%s weight is %d" %(self.name, self.weight))

    def test(self, is_real=True):
        if is_real:
            print("real")
            self.eat()
        else:
            print("not real")

        def say_hello():
            print("hello world")

        say_hello()

