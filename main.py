from expenses_group import Expenses_group
from transaction import Transaction

expense_groups = []


def menu():
    while True:
        print_options()
        option = input("Wybierz jedną z opcji: ")

        match option:
            case "1":
                print_expense_groups()
            case "2":
                expense_group = input("Wybierz grupę wydatków: ")
                expense_groups_names = [eg.name for eg in expense_groups]
                if expense_group in expense_groups_names:
                    expense_group_menu(
                        get_expense_group_by_name(expense_group))
                else:
                    print("Nie ma takiej grupy wydatków!")
                    menu()
            case "3":
                add_expense_group()
            case "4":
                exit()
            case _:
                print("Nie ma takiej opcji!")
                menu()


def print_options():
    print(
        "\n1. Pokaż grupy wydatków\n" +
        "2. Przejdź do grupy wydatków\n" +
        "3. Dodaj grupę wydatków\n" +
        "4. Wyjście\n"
    )


def expense_group_menu(expense_group):
    while True:
        print_expense_group_options()
        option = input("Wybierz jedną z opcji: ")

        match option:
            case "1":
                print(expense_group.people)
            case "2":
                add_person(expense_group)
            case "3":
                expense_group.print_transactions()
            case "4":
                add_transaction(expense_group)
            case "5":
                remove_transaction(expense_group)
            case "6":
                expense_group.print_balances()
            case "7":
                expense_group.print_optimal_transfers()
            case "8":
                menu()
            case _:
                print("Nie ma takiej opcji!")
                expense_group_menu(expense_group)


def print_expense_group_options():
    print(
        "\n1. Pokaż osoby należące do grupy\n" +
        "2. Dodaj osobę do grupy\n" +
        "3. Pokaż transakcje należące do grupy\n" +
        "4. Dodaj transakcję\n" +
        "5. Usuń transakcję\n" +
        "6. Pokaż bilans\n" +
        "7. Oblicz optymalne przelewy\n" +
        "8. Wyjście \n"
    )


def print_expense_groups():
    for expense_group in expense_groups:
        print(expense_group.name)


def add_expense_group():
    title = input("Wpisz nazwę grupy wydatków: ")
    if get_expense_group_by_name(title) != -1:
        raise Exception("Nazwa jest już zajęta!")
    people = [person for person in input(
        "Wpisz osoby należące do grupy oddzielone spacją: ").split()]
    exp_group = Expenses_group(title, people)
    expense_groups.append(exp_group)


def get_expense_group_by_name(name):
    for exp_group in expense_groups:
        if name == exp_group.name:
            return exp_group
    return -1


def add_transaction(expense_group):
    name = input("Wpisz nazwe: ")
    names = [transaction.name for transaction in expense_group.transaction_list]
    if name in names:
        print("Taka transakcja już istnieje!")
        expense_group_menu(expense_group)

    cost = float(input("Wpisz koszt: "))

    people = [person for person in input(
        "Wpisz osoby biorące udział w transakcji oddzielone spacją: ").split()]
    for person in people:
        if person not in expense_group.people:
            print("Wpisana osoba nie należy do tej grupy wydatków!")
            expense_group_menu(expense_group)

    lender = input("Wpisz osobę płacącą: ")
    if lender not in expense_group.people:
        print("Wpisana osoba nie należy do tej grupy wydatków!")

    is_split_equally = input(
        "Wpisz tak jeśli chcesz podzielić koszty po równo lub nie jeśli chcesz zadeklarować różne koszty: ")

    if is_split_equally == "tak":
        expense_group.add_transaction(
            Transaction(name, cost, people, lender, True))
    elif is_split_equally == "nie":
        expense_group.add_transaction(
            Transaction(name, cost, people, lender, False))
    else:
        print("Zła wartość!")
        expense_group_menu(expense_group)


def remove_transaction(expense_group):
    name = input("Wpisz nazwę transakcji, którą chcesz usunąć: ")
    names = [transaction.name for transaction in expense_group.transaction_list]
    if name not in names:
        print("Dana transakcja nie istnieje!")
        expense_group_menu(expense_group)
    else:
        expense_group.remove_transaction(name)


def add_person(expense_group):
    person = input("Wpisz nazwę osoby którą chcesz dodać: ")
    if person in expense_group.people:
        print("Dana osoba już jest wpisana!")
        expense_group_menu(expense_group)
    else:
        expense_group.add_person(person)


if __name__ == '__main__':
    # EXAMPLE 1
    exp_group = Expenses_group(
        "Grupa wydatków 1", ["Alice", "Bill", "Charles"])
    exp_group.add_transaction(Transaction("T1", 10, ["Bill"], "Alice", True))
    exp_group.add_transaction(Transaction("T2", 1, ["Alice"], "Bill", True))
    exp_group.add_transaction(Transaction("T3", 5, ["Charles"], "Bill", True))
    exp_group.add_transaction(Transaction("T4", 5, ["Alice"], "Charles", True))
    expense_groups.append(exp_group)

    # EXAMPLE 2
    exp_group2 = Expenses_group(
        "Grupa wydatków 2", ["Agata", "Hubert", "Bartek"])
    exp_group2.add_transaction(Transaction(
        "T1", 13.24, ["Bartek", "Agata", "Hubert"], "Hubert", True))
    exp_group2.add_transaction(Transaction(
        "T2", 15.23, ["Bartek", "Agata"], "Agata", True))
    exp_group2.add_transaction(Transaction(
        "T3", 123.42, ["Agata", "Hubert", "Bartek"], "Bartek", True))
    expense_groups.append(exp_group2)

    # MENU
    menu()
