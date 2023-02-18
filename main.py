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
Tohle je fakt hnusnej program a kdo ho používá je proklet a o půlnoci přijde modrý dinosaurus a obrátí mu řiť naruby
        """

    def do_vytvor(self, line):
        """Vytvoří nového zákazníka a zařadí ho do evidence"""
        builder = CustomerBuilder()
        builder.first_name = input("Zadej jméno: ")
        builder.last_name = input("Zadej Příjmení: ")
        builder.age = input("Zadej věk: ")
        self.customer_registry.append(builder.build())
        print("Zákazník vytvořen\n")

    def do_vypis(self, line):
        """Vypíše všechny zákazníky v evidenci"""
        print("Seznam zákazníků:")
        """verze 1"""
        my_table = PrettyTable(["Jmeno", "Prijmeni", "Vek"])
        for customer in self.customer_registry:
            my_table.add_row([customer.first_name, customer.last_name, customer.age])
            """print(customer.first_name, customer.last_name, customer.age)"""

        print(my_table)
        # for i in range(0, len(customers)):
        #     print(customers[i].first_name, customers[i].last_name, customers[i].age)
        print(" ")



    def do_vyhledej(self, line):
        """Vyhledá zadaného zákazníka"""
        """sname = input("Zadej hledané jméno: ")
        for customer in self.customer_registry:
            if sname == customer.first_name or sname == customer.last_name:
                print("Je tu")"""

        sname = input("Zadej hledané jméno: ")
        my_table_vypis = PrettyTable(["Jmeno", "Prijmeni", "Vek"])
        for customer in filter(lambda customer: sname in [customer.first_name, customer.last_name], self.customer_registry):
            my_table_vypis.add_row([customer.first_name, customer.last_name, customer.age])

        if len(my_table_vypis.rows) > 0:
            print(my_table_vypis)
        else:
            print("Našel jsen veký hovno")
        return

        for customer in self.customer_registry:
            if sname == customer.first_name or sname == customer.last_name:
                my_table_vypis.add_row([customer.first_name, customer.last_name, customer.age])
                """print(customer.first_name, customer.last_name, customer.age)"""
        else:
            print("Záznam nenalezen")
        print(my_table_vypis)




    def do_exit(self, line):
        return True


if __name__ == '__main__':
    main()
