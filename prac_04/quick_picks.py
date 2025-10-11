import random

NUMBERS_ON_EACH_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    number_of_picks = int(input("How many quick picks?"))
    for i in range(number_of_picks):
        quick_pick = []
        while len(quick_pick) < NUMBERS_ON_EACH_LINE:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in quick_pick:
                quick_pick.append(number)
            quick_pick.sort()

        print(" ".join(f"{number:2}" for number in quick_pick))

main()