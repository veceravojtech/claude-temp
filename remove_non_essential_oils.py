#!/usr/bin/env python3
"""
Skript pro odstranění řádků, které neobsahují 'esenciální olej' v prvním sloupci
"""
import csv
import sys

def remove_non_essential_oil_rows(file_path):
    """Odstraní všechny řádky, které neobsahují 'esenciální olej' v prvním sloupci"""
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

        # Filtruj řádky - ponechej jen ty s "esenciální olej" v prvním sloupci
        filtered_rows = [header]  # Zachovej hlavičku
        removed_rows = []

        for row in data_rows:
            if len(row) > 0:
                first_column = row[0].lower()
                if "esenciální olej" in first_column:
                    filtered_rows.append(row)
                else:
                    removed_rows.append(row)

        # Zapiš filtrované řádky zpět do souboru
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(filtered_rows)

        print(f"Původní počet záznamů: {len(data_rows)}")
        print(f"Odstraněno záznamů: {len(removed_rows)}")
        print(f"Zbývá záznamů: {len(filtered_rows) - 1}")  # -1 pro hlavičku
        print("\nOdstraněné řádky:")
        for row in removed_rows:
            print(f"  - {row[0]}")

    except FileNotFoundError:
        print(f"Soubor {file_path} nebyl nalezen")
    except Exception as e:
        print(f"Chyba při zpracování souboru: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Použití: python3 remove_non_essential_oils.py <cesta_k_csv>")
        sys.exit(1)

    remove_non_essential_oil_rows(sys.argv[1])
