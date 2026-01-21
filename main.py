import products
import store


# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start(store):
    while True:
        print("""
                 Store Menu
                ____________
        
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit
        """)

        choice_input = input("Please choose a number: ")

        if choice_input == "":
            print("Error with your choice! Try again!")
            continue

        if not choice_input.isdigit():
            print("Error with your choice! Try again!")
            continue

        choice = int(choice_input)

        if choice == 1:
            products_in_store = store.get_all_products()
            for index, product in enumerate(products_in_store, start=1):
                print(f"{index}. ", end="")
                product.show()

        elif choice == 2:
            total = store.get_total_quantity()
            print(total)

        elif choice == 3:
            products_in_store = store.get_all_products()
            for index, product in enumerate(products_in_store, start=1):
                print(f"{index}. ", end="")
                product.show()

            shopping_list = []

            while True:
                product_choice = input("Which product # do you want?")
                if product_choice == "":
                    break

                if not product_choice.isdigit():
                    print("Please enter a valid number.")
                    continue

                choice_num = int(product_choice)

                if choice_num < 1 or choice_num > len(products_in_store):
                    print(f"Please enter a number between 1 and {len(products_in_store)}.")
                    continue

                selected_product = products_in_store[choice_num - 1]

                amount_input = input("What amount do you want?")
                if amount_input == "":
                    print("Please enter amount: ")
                    continue

                if not amount_input.isdigit():
                    print("Your input must be a integer")
                    continue

                amount = int(amount_input)

                if amount <= 0:
                    print("Your choice must be a positive interger")
                    continue

                shopping_list.append((selected_product, amount))
                print("Product added to list!")

            if len(shopping_list) == 0:
                print("No items ordered.")
                continue

            total = store.order(shopping_list)
            print("********")
            print(f"Order made! Total payment: ${total}")

        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Error with your choice! Try again!")



start(best_buy)
