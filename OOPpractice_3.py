# class methods

class Person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1


Person.number_of_people = 10 
print(Person.number_of_people)
p1 = Person("jim")
print(p1.number_of_people)


print("-----------------------")


class Person2:

    number_of_people = 0
    def __init__(self, name):
        self.name = name
        Person2.addPerson()
    
    @classmethod
    def numberOfPeople(cls):
        return cls.number_of_people
    
    @classmethod
    def addPerson(cls):
        cls.number_of_people += 1

p3 = Person2("Tim")
print(p3.numberOfPeople())
p4 = Person2("Sam")
print(p4.numberOfPeople())
print(Person2.numberOfPeople()) # I can direct access the property in the class