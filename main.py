# main.py

from utils.table import Table, Seat
from utils.openspace import Openspace
import pandas as pd



def load_colleagues(filepath: str) -> list:
    """
    Load the list of colleagues from a CSV file.

    :param filepath: Path to the CSV file.
    :return: List of names (strings).
    """
    df = pd.read_csv(filepath)
    return df['Name'].tolist()

def main():
    # CSV dosyasından 24 kişiyi yükle
    filepath = "utils/new_colleagues.csv"  # <- utils içine göre path
    colleagues = load_colleagues(filepath)

    # Openspace oluştur, 6 masa, her masa 4 kişilik
    room = Openspace(number_of_tables=6, seats_per_table=4)

    # İnsanları rastgele masalara yerleştir
    room.organize(colleagues)

    # Sonuçları göster
    room.display()
