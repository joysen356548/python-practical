class Student:
    def __init__(self):
        self.__name = "Joy Sen"

    def show(self):
        print("Name:", self.__name)

obj = Student()
obj.show()