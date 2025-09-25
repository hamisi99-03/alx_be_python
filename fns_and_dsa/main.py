from shopping_list_manager import add_item, remove_item, view_list
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
            # Prompt for and add an item
            add_item(shopping_list, input("Enter item to add: "))
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remove_item(shopping_list, input("Enter item to remove: "))
            pass
        elif choice == '3':
            # Display the shopping list
            print("Current Shopping List:", view_list(shopping_list))
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()