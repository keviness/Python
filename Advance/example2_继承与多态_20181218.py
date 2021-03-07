# class-继承与多态-2018.12.18.py

class Animal(object):
    def run(self):
        print("Animal is running....")   
class Dog(Animal):
    def run(self):
        print("dog is running!")
    def eat(self):
        print("dog is eating")
class Cat(Animal):
    def run(self):
        print("cat is running!")
class Tortoise(Animal):
    def run(self):
        print("Tortoise is running slowly!")
dog = Dog()
cat = Cat()
def run_twice(animal):
    animal.run()
    animal.run()  
