# Program 7: Conditional menu
choice = input("Enter 'E' or 'O': ").upper()
if choice == 'E':
    print("Even")
elif choice == 'O':
    print("Odd")
else:
    print("Invalid choice")
