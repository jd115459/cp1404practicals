#1.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

#2.
in_file = open("name.txt", "r")
name = in_file.read()
print(f" Hi {name}")
in_file.close()

#3.
with open("numbers.txt", "r") as in_file:
    number_one = int(in_file.readline())
    number_two = int(in_file.readline())
    print(number_one + number_two)

#4.
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)

