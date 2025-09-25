def password_stars():
    minimum_length = 6
    password = input("Enter your password: ")
    while len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters long")
        password = input("Enter your password: ")

    print('*' * len(password))

password_stars()
