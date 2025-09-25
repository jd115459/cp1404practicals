def main():
    minimum_length = 6
    password = get_password(minimum_length)

    password_length(password)


def password_length(password: str):
    print('*' * len(password))


def get_password(minimum_length: int) -> str:
    password = input("Enter your password: ")
    while len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters long")
        password = input("Enter your password: ")
    return password


main()
