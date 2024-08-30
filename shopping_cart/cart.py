import json
from dataclasses import dataclass, field
from shopping_cart.item import Item
from shopping_cart.random_number_utils import RandomUtils
from shopping_cart.file_io import Fstream

@dataclass
class Cart:
    database_path: str
    isEmpty: bool = True
    isActive: bool = False
    id: str = field(init=False, default_factory=RandomUtils.generate_random_id)
    items: list[Item] = field(init=False, default_factory=list)

    def get_all_items(self, verbose=0)->dict:
        """
        Reads and returns a hash map with all the available items in the database.

        Args:
            if verbose is set to 1, it will print all the items.

        Returns:
            A hash map with all the items in the database
        """
        data_file = Fstream.load_json_file(self.database_path)
        try:
            if verbose == 1:
                Fstream.print_json_structure(data_file)
                return data_file
            else:
                return data_file
        except:
            raise ValueError("The value for verbose has to be 0 or 1")

    def search_items(self, query: str)->list[Item]:
        """
        Searches for items in the cart based on a query.

        Args:
            query (str): The search query.

        Returns:
            list[Item]: A list of items that match the search query.
        """
        data = Fstream.load_json_file(self.database_path)
        
        # Search for items matching the query
        matching_items = []
        for item_id, item_data in data["Items"].items():
            item = Item(item_data["name"], item_data["type"], item_data["price"])
            if query.lower() in item.search_string.lower():
                matching_items.append(item)
        
        if len(matching_items) == 0:
            print("No items found")
        else:
            for item in matching_items:
                print(f"Found: {item.name} ({item.type}) - $({item.price})")
        
        return matching_items

    def get_total_item_count(self)->int:
        """
        Returns the total number of items in the cart.

        Returns:
            int: The total number of items in the cart.
        """
        data = self.get_all_items()
        return len(data["Items"].items())



