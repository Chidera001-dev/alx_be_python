def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            list_name = input("Enter item to add: ")
            shopping_list.append(list_name)
            print(f"'{list_name}' added to your list.")
        elif choice == '2':
            list_name = input("Enter item to remove: ")
            if list_name in shopping_list:
                shopping_list.remove(list_name)
                print(f"'{list_name}' removed from your list.")
            else:
                print(f"'{list_name}' not found in your list.")
        elif choice == '3':
            print("\nYour Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()