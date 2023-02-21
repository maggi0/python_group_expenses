class Transfer:
    def __init__(self, borrower, lender, amount):
        self.borrower = borrower
        self.lender = lender
        self.amount = amount

    def print_transfer(self):
        print("{} przelewa {:.2f}$ dla {}".format(
            self.borrower, float(self.amount), self.lender))
