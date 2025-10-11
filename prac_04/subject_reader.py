"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_data= load_subject_data(FILENAME)
    display_subject_data(subject_data)


def load_subject_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subjects = []

    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")

        subjects.append(parts)
    input_file.close()
    return subjects

def display_subject_data(subject_data):
    for subject in subject_data:
        subject_code = subject[0]
        lecturer_name = subject[1]
        number_of_students = subject[2]
        print(f"{subject_code} is taught by {lecturer_name} and has {number_of_students} students.")


main()