class Father:
    def show(self):
        print("This is Parent Class")

class Son(Father):
    pass

obj = Son()
obj.show()