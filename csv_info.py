#!/usr/bin/env python3
"""
Skript pro analýzu CSV souborů - správně počítá záznamy i u víceřádkových polí
"""
import csv
import sys

def analyze_csv(file_path):
    """Analyzuje CSV soubor a vypíše základní informace"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) == 0:
                print("Soubor je prázdný")
                return

            # Hlavička
            header = rows[0]
            data_rows = rows[1:]

            print(f"Soubor: {file_path}")
            print(f"Celkem řádků (včetně hlavičky): {len(rows)}")
            print(f"Počet záznamů: {len(data_rows)}")
            print(f"Počet sloupců: {len(header)}")
            print(f"\nSloupce:")
            for i, col in enumerate(header, 1):
                print(f"  {i}. {col}")

            # Ukázka prvních pár záznamů
            print(f"\nPrvních 5 záznamů:")
            for i, row in enumerate(data_rows[:5], 1):
                print(f"\nZáznam {i}:")
                for col_name, value in zip(header, row):
                    # Zkrácení dlouhých hodnot
                    display_value = value[:100] + "..." if len(value) > 100 else value
                    print(f"  {col_name}: {display_value}")

    except FileNotFoundError:
        print(f"Soubor {file_path} nebyl nalezen")
    except Exception as e:
        print(f"Chyba při čtení souboru: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Použití: python3 csv_info.py <cesta_k_csv>")
        sys.exit(1)

    analyze_csv(sys.argv[1])
