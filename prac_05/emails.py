"""
Emails
Estimate: 25mins
Actual: 33mins
"""

def main():
    email_to_name = {"jackson scrivener": "jackson.scrivener@my.jcu.edu.au", "ryan smith": "ryansmithy123@gmail.com",
                     "bella ford": "bellsf435@hotmail.com"}
    email = input("Enter your email: ")
    while email !="":
        name = get_name_from_email(email)
        check_name = input(f"Is your name {name}? (y/n): ")
        if check_name.lower() != "y" and check_name !="":
            name = input("Enter your name: ")
        email_to_name[email] = name
        email = input("Enter your email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")



def get_name_from_email(email):
    """Extract expected name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()