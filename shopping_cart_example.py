from shopping_cart.item import Item
from shopping_cart.cart import Cart

if __name__ == "__main__":

    #the main database for the cart to pass to the class
    database = "./database.json"
    my_cart = Cart(database)

    #search for an item
    results = my_cart.search_items("apple")

    #get the total amount of items in the cart
    total_item_count = my_cart.get_total_item_count()
    print(f"Total item count: {total_item_count}")

    print("------------------------")

    #Create an Item object so it can be added to the cart
    milk = Item("milk","liquid",1.23)
    my_cart.add_item_to_cart(milk)

    #get all the items in the cart
    print("------------------------")
    my_cart.get_all_items(verbose=1)

    print("------------------------")

    #remove items by name or type
    my_cart.remove_item_from_cart("milk")
    print("------------------------")

    my_cart.get_all_items(verbose=1)