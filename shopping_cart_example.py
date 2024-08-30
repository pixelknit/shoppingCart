from shopping_cart.item import Item
from shopping_cart.cart import Cart

if __name__ == "__main__":

    #apple = Item("apple","fruit",0.3333)
    database = "./database.json"
    my_cart = Cart(database)
    #my_cart.get_all_items(verbose=1)
    results = my_cart.search_items("apple")
    total_item_count = my_cart.get_total_item_count()
    print(f"Total item count: {total_item_count}")