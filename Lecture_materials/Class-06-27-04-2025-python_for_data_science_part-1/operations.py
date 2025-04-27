
class Person:

    def __init__(self, name, age, nationality, skills=[]):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.skills = skills

    def show_skills(self):
        print(f"Skills are: {self.skills}")

    def show_name(self):
        print(f"Name is: {self.name}")


class Employee(Person):

    def __init__(self, name, age, nationality, company_name, salary, manager_name, skills=[]):
        self.company_name = company_name
        self.salary = salary
        self.manager_name = maanager_name
        self.name = name
        self.age = age
        self.nationality = nationality
        self.skills = skills

        super().__init__(self.name, self.age, self.nationality, self.skills)

    def show_salary(self):
        print(f"salary = {self.salary}")


def do_some_operation(number):

    value = number**2 + number + 2

    return value