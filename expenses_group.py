from transfer import Transfer


class Expenses_group:

    def __init__(self, name, people):
        self.name = name
        self.people = people
        self.transaction_list = []

    def add_person(self, person):
        self.people.append(person)

    def add_transaction(self, transaction):
        self.transaction_list.append(transaction)

    def remove_transaction(self, name):
        for transaction in self.transaction_list:
            if transaction.name == name:
                self.transaction_list.remove(transaction)

    def print_transactions(self):
        if(len(self.transaction_list) == 0):
            print("Grupa nie ma żadnych transakcji!")
        for i, transaction in enumerate(self.transaction_list):
            print("Nazwa: " + transaction.name)
            print("Koszt: " + str(transaction.cost))
            print("Osoby: " + str(transaction.people))
            print("Osoba płacąca: " + transaction.lender)
            print("Koszty osób: " + str(transaction.expenses))
            print()

    def print_balances(self):
        print(self.calculate_balances())

    def print_optimal_transfers(self):
        balances = self.calculate_balances()
        transfers = self.calculate_transfers(balances)
        for transfer in transfers:
            transfer.print_transfer()

    def calculate_balances(self):
        balances = {person: 0 for person in self.people}
        for transaction in self.transaction_list:
            for person, amount in transaction.expenses.items():
                balances[transaction.lender] += amount
                balances[person] -= amount

        return balances

    def calculate_transfers(self, balances):
        borrowers = {k: v for k, v in balances.items() if v < 0}
        lenders = {k: v for k, v in balances.items() if v > 0}

        sorted_borrowers = dict(
            sorted(borrowers.items(), key=lambda x: x[1], reverse=False))
        sorted_lenders = dict(
            sorted(lenders.items(), key=lambda x: x[1], reverse=True))

        transfers = []

        while not (len(sorted_borrowers) == 0 or len(sorted_lenders) == 0):
            first_borrower = list(sorted_borrowers.keys())[0]
            first_lender = list(sorted_lenders.keys())[0]
            amount = min(abs(sorted_borrowers[first_borrower]), abs(
                sorted_lenders[first_lender]))

            transfers.append(Transfer(first_borrower, first_lender, amount))

            sorted_borrowers.update(
                {first_borrower: sorted_borrowers[first_borrower] + amount})
            sorted_lenders.update(
                {first_lender: sorted_lenders[first_lender] - amount})

            if sorted_borrowers[first_borrower] == 0.0:
                del sorted_borrowers[list(sorted_borrowers.keys())[0]]
            else:
                del sorted_lenders[list(sorted_lenders.keys())[0]]

        return transfers
