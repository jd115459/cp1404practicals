"""
My Guitars
Read guitars from file, sort, display and save
"""

from prac_07.guitar import Guitar

def load_guitars(filename):
    guitars = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                name = parts[0]
                year = int(parts[1])
                cost = float(parts[2])
                guitars.append(Guitar(name, year, cost))
    return guitars

def save_guitars(guitars, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=file)

def display_guitars(guitars):
    for i, guitar in enumerate(guitars, start=1):
        print(f"{i}: {guitar}")

def get_new_guitars():
    new_guitars = []
    name = input("Guitar Name: ").strip()
    while name != "":
        year = int(input("Guitar Year: "))
        cost = float(input("Guitar Cost: "))
        new_guitars.append(Guitar(name, year, cost))
        name = input("Guitar Name: ").strip()
    return new_guitars




def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)
    display_guitars(guitars)
    new_guitars = get_new_guitars()

    for guitar in new_guitars:
        guitars.append(guitar)

    guitars.sort()

    print("\nSorted Guitars:")
    display_guitars(guitars)

    save_guitars(guitars, filename)
    print(f"\nSaved {len(guitars)} guitars to {filename}")


if __name__ == "__main__":
    main()
