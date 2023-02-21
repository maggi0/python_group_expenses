class Transaction:

    def __init__(self, name, cost, people, lender, is_split_equally):
        self.name = name
        self.cost = cost
        self.people = people
        self.lender = lender
        self.expenses = {}
        if is_split_equally:
            self.calculate_expenses_for_split_equally()
        else:
            self.declare_costs()

    def declare_costs(self):
        for person in self.people:
            self.expenses[person] = float(
                input("Podaj koszt dla " + str(person) + ": "))

        if round(sum(self.expenses.values()), 2) != round(self.cost, 2):
            print("Całkowity koszt nie jest równy kosztom osób! Spróbuj jeszcze raz.")
            self.declare_costs()

    def calculate_expenses_for_split_equally(self):
        for person in self.people:
            if person != self.lender:
                self.expenses[person] = self.cost / len(self.people)
