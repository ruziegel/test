class Profile:
    def __init__(self, name):
        self.prof_name = name

    def info(self):
        return ''

    def describe(self):
        print(self.prof_name, self.info())


class Vacancy(Profile):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def info(self):
        return f'Предлагаемая зарплата: {self.salary}'


class Resume(Profile):
    def __init__(self, name, exp):
        super().__init__(name)
        self.exp = exp

    def info(self):
        return f'Стаж работы: {self.exp}'
