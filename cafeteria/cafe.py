def display_menu(menu_items, title):
    print(f"\n--- {title} Menu ---")
    for item, price in menu_items.items():
        print(f"{item.title()} - ₹{price}")
    print("\n")


def main():
    # Menu Data
    breakfast_menu = {
        "idli": 30,
        "mysore bonda": 40
    }

    lunch_menu = {
        "veg fried rice": 70,
        "paneer fried rice": 90,
        "mushroom fried rice": 90,
        "veg noodles": 70,
        "veg manchurian": 80,
        "chicken fried rice": 80,
        "chicken noodles": 80,
        "chicken manchurian": 80
    }

    snacks_menu = {
        "veg curry puff": 25,
        "egg puff": 30,
        "chicken puff": 45,
        "veg burger": 50,
        "chicken burger": 60,
        "choco lava cake": 60,
        "veg sandwich": 40,
        "chicken sandwich": 50
    }

    cakes_milkshakes_menu = {
        "choco chip cake": 50,
        "chocolate cake": 40,
        "oreo milkshake": 90,
        "kitkat milkshake": 90
    }

    while True:
        print("\n==============================")
        print("     CAFETERIA MENU VIEWER     ")
        print("==============================")
        print("1. View Breakfast Menu")
        print("2. View Lunch Menu")
        print("3. View Snacks Menu")
        print("4. View Cakes & Milkshakes")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_menu(breakfast_menu, "Breakfast")
        elif choice == '2':
            display_menu(lunch_menu, "Lunch")
        elif choice == '3':
            display_menu(snacks_menu, "Snacks")
        elif choice == '4':
            display_menu(cakes_milkshakes_menu, "Cakes & Milkshakes")
        elif choice == '5':
            print("\nThank you for using the Cafeteria Menu Viewer. Have a great day!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")


if __name__== "__main__":
    main()
