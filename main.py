from cmd import Cmd

from prettytable import PrettyTable

from customer import CustomerBuilder


def main():
    """tohle je main"""
    customer_registry = []
    MyCommandLine(customer_registry).cmdloop()


class MyCommandLine(Cmd):
    """commandline"""

    def __init__(self, customer_registry):
        super(MyCommandLine, self).__init__()
        self.customer_registry = customer_registry
        self.prompt = "> "
        self.intro = """
Vítejte v evidenci osob, pro nápovědu vypište help, pro konec exit
        """

    def do_vytvor(self, line):
        """Vytvoří nového zákazníka a zařadí ho do evidence"""
        builder = CustomerBuilder()
        builder.first_name = input("Zadej jméno: ")
        builder.last_name = input("Zadej Příjmení: ")
        builder.age = input("Zadej věk: ")
        builder.phone_number = input("Zadej tel. č.: ")
        self.customer_registry.append(builder.build())
        print("Zákazník vytvořen\n")

    def do_vypis(self, line):
        """Vypíše všechny zákazníky v evidenci"""
        print("Seznam zákazníků:")
        my_table = PrettyTable(["Jmeno", "Prijmeni", "Vek", "Tel. č."])
        for customer in self.customer_registry:
            my_table.add_row([customer.first_name, customer.last_name, customer.age, customer.phone_number])
            """print(customer.first_name, customer.last_name, customer.age)"""

        print(my_table)
        # for i in range(0, len(customers)):
        #     print(customers[i].first_name, customers[i].last_name, customers[i].age)
        print(" ")


    def do_vyhledej(self, line):
        """Vyhledá zadaného zákazníka"""
        sname = input("Zadej hledané jméno: ")
        my_table_vypis = PrettyTable(["Jmeno", "Prijmeni", "Vek", "Tel. č."])
        for customer in filter(lambda customer: sname in [customer.first_name, customer.last_name], self.customer_registry):
            my_table_vypis.add_row([customer.first_name, customer.last_name, customer.age, customer.phone_number])

        if len(my_table_vypis.rows) > 0:
            print(my_table_vypis)
        else:
            print("Záznam nenalezen")


    def do_exit(self, line):
        return True


if __name__ == '__main__':
    main()
