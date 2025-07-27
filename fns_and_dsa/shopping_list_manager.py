def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()

        # Handle non-numeric input
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added to shopping list.")

        elif choice == 2:
            remove_item = input("Enter item to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"'{remove_item}' removed from shopping list.")
            else:
                print(f"'{remove_item}' not found in the list.")

        elif choice == 3:
            if shopping_list:
                print("Your Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
