#!/usr/bin/env python3
"""
Skript pro nalezení řádků, které neobsahují 'esenciální olej' v prvním sloupci
"""
import csv
import sys

def find_non_essential_oil_rows(file_path):
    """Najde všechny řádky, které neobsahují 'esenciální olej' v prvním sloupci"""
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

            # Najdi řádky bez "esenciální olej" v prvním sloupci
            non_essential_oil_rows = []
            for i, row in enumerate(data_rows, 1):
                if len(row) > 0:
                    first_column = row[0].lower()
                    if "esenciální olej" not in first_column:
                        non_essential_oil_rows.append((i, row))

            print(f"Celkem záznamů: {len(data_rows)}")
            print(f"Záznamy BEZ 'esenciální olej' v prvním sloupci: {len(non_essential_oil_rows)}")
            print(f"Záznamy S 'esenciální olej' v prvním sloupci: {len(data_rows) - len(non_essential_oil_rows)}")
            print("\n" + "="*80)
            print("Řádky, které NEOBSAHUJÍ 'esenciální olej' v prvním sloupci:")
            print("="*80 + "\n")

            for row_num, row in non_essential_oil_rows:
                print(f"Řádek {row_num}:")
                for col_name, value in zip(header, row):
                    # Zkrácení dlouhých hodnot
                    display_value = value[:100] + "..." if len(value) > 100 else value
                    print(f"  {col_name}: {display_value}")
                print()

    except FileNotFoundError:
        print(f"Soubor {file_path} nebyl nalezen")
    except Exception as e:
        print(f"Chyba při čtení souboru: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Použití: python3 find_non_essential_oils.py <cesta_k_csv>")
        sys.exit(1)

    find_non_essential_oil_rows(sys.argv[1])
