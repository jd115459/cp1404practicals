"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = float(input("Enter score: "))
    result = score_result(score)
    print(result)

random_score = random.uniform(0, 100)
print(f"Random score: {random_score:.2f}\n {score_result(random_score)}")

main()