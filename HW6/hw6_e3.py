class Worker:
    name: str
    surname: str
    position: str
    _income: dict()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Full name: {self.name} {self.surname}")

    def get_total_income(self):
        total_income = self._income.get('wage') + self._income.get('bonus')
        print(f"Monthly income: {total_income}")


john = Position(name='John', surname='Doe', position='IT Specialist', wage=23500, bonus=12000)
print(f"Basic data: {john.name} {john.surname}, {john.position}")
john.get_full_name()
john.get_total_income()
