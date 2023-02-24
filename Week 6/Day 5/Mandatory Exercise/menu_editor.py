from restaurant import MenuItem,run_query
import psycopg2

def load_manager(*items):
    menu_items = []
    for item in items:
        name, price = item
        menu_items.append(MenuItem(name, price))

    return menu_items

def show_user_menu():
    while True:
        print(f"MENU\n(a) Add an item\n(d) Delete an Item\n(v) View an item\n(x) Exit")
        choice = input("Choose an option: " )
        if choice == 'a':
            add_item_to_menu()

        elif choice == 'd':
            remove_item_from_menu()

        elif choice == 'v':
           show_restaurant_menu()
        
        elif choice == "x":
           show_restaurant_menu()
           break

        else:
         print('Wrong Input Try again')

def add_item_to_menu():
    name = input("What item do you want: ")
    price = int(input("How much is the item: "))
    addition = MenuItem(name,price)
    addition.save()
    print("Item was added successfully")

def remove_item_from_menu():
    name = input("What item do you want to remove : ")
    price = None
    removal = MenuItem(name, price)
    removal.delete()
    print("Item was removed successfully")

def show_restaurant_menu():
    name = None
    price = None
    menu = MenuItem(name, price)
    print(menu.all())

load_manager()
show_user_menu()