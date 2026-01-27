import products
import store


# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def print_menu():
    print("""
             Store Menu
            ____________

    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit
    """)

def list_products(store_obj):
    products_in_store = store_obj.get_all_products()
    for index, product in enumerate(products_in_store, start=1):
        print(f"{index}. ", end="")
        product.show()
    return True

def show_total_amount(store_obj):
    print(store_obj.get_total_quantity())
    return True


def make_order(store_obj):
    products_in_store = store_obj.get_all_products()
    for index, product in enumerate(products_in_store, start=1):
        print(f"{index}. ", end="")
        product.show()

    shopping_list = []

    while True:
        product_choice = input("Which product # do you want? ")
        if product_choice == "":
            break

        if not product_choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice_num = int(product_choice)
        if choice_num < 1 or choice_num > len(products_in_store):
            print("Invalid product number.")
            continue

        selected_product = products_in_store[choice_num - 1]

        amount_input = input("What amount do you want? ")
        if not amount_input.isdigit():
            print("Please enter a valid amount.")
            continue

        amount = int(amount_input)
        if amount <= 0:
            print("Amount must be positive.")
            continue

        shopping_list.append((selected_product, amount))
        print("Product added to list!")

    if len(shopping_list) == 0:
        print("No items ordered.")
        return True

    try:
        total = store_obj.order(shopping_list)
        print("********")
        print(f"Order made! Total payment: ${total}")
    except (ValueError, TypeError) as e:
        print(f"Order failed: {e}")

    return True


def quit_store(store_obj):
    print("Goodbye!")
    return False


def start(store):
    actions = {
        1: list_products,
        2: show_total_amount,
        3: make_order,
        4: quit_store,
    }

    running = True
    while running:
        print_menu()

        choice_input = input("Please choose a number: ")
        if not choice_input.isdigit():
            print("Error with your choice! Try again!")
            continue

        choice = int(choice_input)
        action = actions.get(choice)

        if action is None:
            print("Error with your choice! Try again!")
            continue

        running = action(store)


start(best_buy)
