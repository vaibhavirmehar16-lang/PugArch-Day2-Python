class Employee:

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def display(self):
        print("Name:", self._name)
        print("Salary:", self._salary)


class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display_manager(self):
        self.display()
        print("Team Size:", self.team_size)


manager = Manager("Priya", 80000, 8)

manager.display_manager()