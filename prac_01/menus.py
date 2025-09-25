Menu = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter Your Name: ")
print(Menu)
choice = input("Enter Your Choice: ")
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid Choice!")
    choice = input("Enter Your Choice: ")

print("Finished.")