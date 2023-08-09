class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def form_name(self):
        return f"{self.name} is {self.age} years old"


maria = User("Maria", 30)
print(maria.form_name())