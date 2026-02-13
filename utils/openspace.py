import random
from utils.table import Table


class Openspace:
    """
    This class represents the whole openspace.
    """

    def __init__(self, number_of_tables: int = 6, seats_per_table: int = 4) -> None:
        """
        Initialize the openspace with tables.
        """
        self.number_of_tables = number_of_tables
        self.tables = []

        for i in range(number_of_tables):
            table = Table(seats_per_table)
            self.tables.append(table)

    def organize(self, names: list[str]) -> None:
        """
        Randomly assign people to tables.
        """
        random.shuffle(names)

        for name in names:
            placed = False
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    placed = True
                    break

            if not placed:
                print(f"No free seat for {name}")

    def display(self) -> None:
        """
        Display the tables and their seats.
        """
        for index, table in enumerate(self.tables, start=1):
            print(f"Table {index}: {table}")
            print(f"Free seats: {table.left_capacity()}")
            print("-" * 30)

    def store(self, filename: str) -> None:
        """
        Store the result in an Excel file.
        """
        import pandas as pd

        data = {}

        for index, table in enumerate(self.tables, start=1):
            data[f"Table {index}"] = [str(seat) for seat in table.seats]

        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
