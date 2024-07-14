class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what to say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print("nyan~ nyan~")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. I have {self.color} color.")

class Dog(Pet):
    def speak(self):
        print("WOLF ! WOLF")

class Fish(Pet):
    pass

p = Pet("JJ", 23)
p.speak()

c = Cat("Eric", 66, "Orange")
c.speak()
c.show()

d = Dog("Jon",20)
d.speak()

f = Fish("Bubble", 2)
f.show()
f.speak()

