class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber


student1 = Student("John", 20, "11B")
student2 = Student("Jane", 19, "12A")
student3 = Student("Mike", 21, "11A")
student4 = Student()
student5 = Student("Kate", 18, "12B")

print(student1.getName())
print(student2.getAge())
print(student3.getGroupNumber())

student4.setNameAge("Alice", 22)
student4.setGroupNumber("12B")

print(student4.getName())
print(student4.getAge())
print(student4.getGroupNumber())