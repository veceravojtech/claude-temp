#!/usr/bin/env python3
import csv

# Řádky ke smazání (čísla řádků v CSV, kde 1 je hlavička, 2 je první datový řádek)
rows_to_delete = {5, 6, 51}

with open('bewit.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

# Odfiltrovat řádky (header je index 0, data začínají od indexu 1)
filtered_rows = [rows[0]]  # hlavička
for i, row in enumerate(rows[1:], start=2):  # data začínají od řádku 2
    if i not in rows_to_delete:
        filtered_rows.append(row)

# Zapsat zpět
with open('bewit.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(filtered_rows)

print(f"Smazáno {len(rows_to_delete)} řádků. Nový počet záznamů: {len(filtered_rows) - 1}")
