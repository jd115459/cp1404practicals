def get_valid_score():
    score = float(input("Enter  (0-100): "))
    result = score_result(score)
    while score < 0 or score > 100:
        print("Invalid score, try again")
        score = float(input("Enter score (0-100): "))
    return score

def print_stars(score):
    print("*" * int(score))


def score_result(score):
    """Return a string describing the score result."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    MENU = """\n
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    score = get_valid_score()

    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(score_result(score))
        elif choice == "S":
            print_stars(score)
        elif choice != "Q":
            print("Invalid choice, try again")

    print("Farewell")


main()
