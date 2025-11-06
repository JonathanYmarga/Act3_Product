# Product List Manager
# Activity 3 - List Operations, Sorting, and Searching

def display_products(products, prices):
    print("\n----------------------------------------")
    print("Product List:")
    print(products)
    print("Price List:")
    print(prices)
    print("----------------------------------------")

def main():
    products = []
    prices = []

    # Input and store data
    n = int(input("Enter number of products: "))
    for i in range(n):
        product = input(f"Enter product {i + 1} name: ")
        while True:
            try:
                price = float(input(f"Enter price of {product}: "))
                break
            except ValueError:
                print("Invalid price. Please enter a number.")
        products.append(product)
        prices.append(price)

    display_products(products, prices)

    # Processing loop
    while True:
        print("\nChoose an action:")
        print("1 - Add a new product")
        print("2 - Remove a product")
        print("3 - Sort products by price")
        print("4 - Search for a product")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add product
            new_product = input("Enter new product name: ")
            while True:
                try:
                    new_price = float(input(f"Enter price of {new_product}: "))
                    break
                except ValueError:
                    print("Invalid price. Please enter a number.")
            products.append(new_product)
            prices.append(new_price)
            print(f"{new_product} added successfully!")

        elif choice == "2":
            # Remove product
            name = input("Enter the product name to remove: ")
            if name in products:
                index = products.index(name)
                products.pop(index)
                prices.pop(index)
                print(f"{name} removed successfully!")
            else:
                print("Product not found!")

        elif choice == "3":
            # Sort products
            print("\nSort by price:")
            print("1 - Ascending")
            print("2 - Descending")
            sort_choice = input("Enter your choice: ")
            if sort_choice == "1":
                combined = sorted(zip(prices, products))
            else:
                combined = sorted(zip(prices, products), reverse=True)
            prices, products = zip(*combined)
            products = list(products)
            prices = list(prices)
            print("Products sorted by price!")

        elif choice == "4":
            # Search product
            search_name = input("Enter product name to search: ")
            if search_name in products:
                index = products.index(search_name)
                print(f"Product Found!\n{search_name} - Price: {prices[index]}")
            else:
                print("Product not found!")

        else:
            print("Invalid choice.")

        display_products(products, prices)

        cont = input("Do you want to continue? (yes/no): ").lower()
        if cont != "yes":
            print("\nProgram terminated.")
            print("Thank you for using the Product List Manager!")
            break


if __name__ == "__main__":
    main()
