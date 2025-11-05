#!/usr/bin/env python3
"""
Skript pro kontrolu latinských názvů v bewit.csv
"""
import csv
import re

def is_valid_latin_name(name):
    """
    Kontroluje, zda je text platný latinský název byliny.
    Latinský název by měl:
    - Obsahovat hlavně latinská písmena (a-z, A-Z)
    - Neobsahovat české znaky (ž, š, č, ř, ě, ý, á, í, é, ú, ů, ď, ť, ň)
    - Mít typickou strukturu (většinou 2-3 slova, začínající velkým písmenem)
    """
    if not name or name.strip() == "":
        return False, "prázdné pole"

    # České znaky
    czech_chars = re.search(r'[žščřďťňěýáíéúů]', name, re.IGNORECASE)
    if czech_chars:
        return False, "obsahuje české znaky"

    # Čeština/běžná slova
    czech_words = [
        'zázračné', 'vyladění', 'veselé', 'vánoce', 'směs', 'olej',
        'esenciální', 'bylinná', 'vonný', 'čistý', 'organický',
        'bio', 'přírodní', 'květinová', 'dřevitá', 'svěží',
        'harmonizace', 'povzbuzení', 'uklidnění', 'očista',
        'jarní', 'letní', 'podzimní', 'zimní', 'radost',
        'láska', 'síla', 'energie', 'klid', 'rovnováha',
        'ochrana', 'čistota', 'harmonie', 'vitalita'
    ]

    name_lower = name.lower()
    for word in czech_words:
        if word in name_lower:
            return False, f"obsahuje české slovo '{word}'"

    # Typická struktura latinského názvu: Genus species (případně subspecies/var.)
    # Mělo by začínat velkým písmenem a pokračovat malými
    words = name.split()
    if len(words) == 0:
        return False, "žádná slova"

    # První slovo by mělo začínat velkým písmenem
    if not words[0][0].isupper():
        return False, "nezačíná velkým písmenem"

    # Kontrola, že nejsou všechna písmena velká (kromě zkratek jako var., subsp.)
    common_abbrevs = ['var.', 'subsp.', 'f.', 'cv.', 'x']
    for word in words:
        if word.lower() not in common_abbrevs and word.isupper() and len(word) > 1:
            return False, "obsahuje slovo psané velkými písmeny"

    return True, "OK"

def check_latin_names(file_path):
    """Zkontroluje všechny latinské názvy v CSV"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            invalid_rows = []
            row_num = 2  # Začínáme od 2 (1 je hlavička)

            for row in reader:
                latin_name = row.get('latinský nazev', '').strip()
                is_valid, reason = is_valid_latin_name(latin_name)

                if not is_valid:
                    invalid_rows.append({
                        'row_num': row_num,
                        'nazev': row.get('nazev', ''),
                        'latinský_nazev': latin_name,
                        'reason': reason
                    })

                row_num += 1

            # Výpis výsledků
            if invalid_rows:
                print(f"Nalezeno {len(invalid_rows)} řádků s neplatným latinským názvem:\n")
                print("=" * 100)

                for item in invalid_rows:
                    print(f"\nŘádek {item['row_num']}:")
                    print(f"  Název produktu: {item['nazev']}")
                    print(f"  Latinský název: '{item['latinský_nazev']}'")
                    print(f"  Problém: {item['reason']}")
                    print("-" * 100)

                print(f"\nCelkem problematických řádků: {len(invalid_rows)}")
            else:
                print("Všechny latinské názvy jsou v pořádku!")

    except FileNotFoundError:
        print(f"Soubor {file_path} nebyl nalezen")
    except Exception as e:
        print(f"Chyba při čtení souboru: {e}")

if __name__ == "__main__":
    check_latin_names('bewit.csv')
