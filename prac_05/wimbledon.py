"""
Wimbledon
Estimate: 25mins
Actual:
"""
import csv

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def main():
    records = load_records(FILENAME)
    champion_to_country, countries = process_records(records)
    display_results(champion_to_country, countries)

def process_records(records):
    champion_to_country = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_country[record[INDEX_CHAMPION]] +=1
        except KeyError:
            champion_to_country[record[INDEX_CHAMPION]] = 1
    return champion_to_country, countries

def display_results(champion_to_country, countries):
    print("Wimbledon Champions:")
    for name, country in champion_to_country.items():
        print(name, country)
    print(f"\nThese {len(countries)} have won:")
    print(", ".join(sorted(countries)))


def load_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
        return records

main()