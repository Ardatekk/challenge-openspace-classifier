# main.py
# This is a simple Openspace Organizer script
# It reads colleagues from a CSV file and assigns them randomly to tables
# Author: Arda Tekelli
# Level: Beginner / Amateur style

from utils.table import Table, Seat
from utils.openspace import Openspace
import pandas as pd

# Path to the CSV file containing colleagues
filepath = "utils/new_colleagues.csv"

def load_colleagues(filepath: str) -> list:
    """
    Load a list of colleagues from a CSV file.

    :param filepath: Path to the CSV file
    :return: List of names as strings
    """
    df = pd.read_csv(filepath)
    return df['Name'].tolist()

def main():
    """
    Main function to run the openspace organizer.
    """
    # Step 1: Load colleagues from CSV
    colleagues = load_colleagues(filepath)

    # Step 2: Create an Openspace with 6 tables, 4 seats per table
    room = Openspace(number_of_tables=6, seats_per_table=4)

    # Step 3: Randomly assign colleagues to tables
    room.organize(colleagues)

    # Step 4: Display table assignments and free seats
    room.display()

    # Optional: Save the result to Excel (uncomment if needed)
    # room.store("assigned_openspace.xlsx")

if __name__ == "__main__":
    main()
