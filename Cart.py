""" Cart.py
This module Contains the Cart Class.

Author(s):
    Redbubble Applicant

Date Created:
    October 1st, 2018
"""
# ---------------------------------------------------------------------------- #
# Import Statements for the Necessary Packages / Modules
# ---------------------------------------------------------------------------- #
from ProductItem import ProductItem

class Cart:
    """
    Cart Class - Represents a Shopping Cart in the Redbubble Universe.

    Attributes:
        _cart_json (JSON Object): JSON Object Represented in the Cart JSON 
        File.
        _list_of_ProductItems (List): Contains Product Items in a List.
    """
    def __init__(self, cart_json):
        """
        Constructor for the Cart Class.
        
        Args:
            self (none): None.
            cart_json (JSON Object): JSON Object Represented in the Cart JSON 
            File.
        
        Returns:
            (void): No return value. Just sets member variables.
        """
        self._cart_json = cart_json #Can Be Useful in Future
        self._product_counts = {}
        self._list_of_ProductItems = self.make_product_items(cart_json)

    def make_product_items(self, cart_json):
        """
        Retrieves the Product Items from the Cart Json File.
        
        Args:
            self (none): None.
            cart_json (JSON Object): JSON Object Represented in the Cart JSON 
            File.
        Returns:
            (List): Contains Product Items in a List.
        """
        rs = []
        for product in cart_json:
            #From Cart Schema (THIS MAY CHANGE), we need Product Type, Options,
            #Artist-Markup, and Quantity
            product_type = product['product-type']
            options = product['options']
            artist_markup = product['artist-markup']
            quantity = product['quantity']
            new_product = ProductItem(product_type, options, artist_markup, \
            quantity)
            if(product_type not in self._product_counts):
                self._product_counts[product_type] = quantity
            else:
                self._product_counts[product_type] = self._product_counts[product_type] + quantity
            rs.append(new_product)
        return rs;
    
    def get_product_quant_dict(self):
        return self._product_counts

    def get_product_items(self):
        """
        Public Accessor for the Member Variable: Product Items List.
        *More Memory Efficient for Product Items if make_product_items() was 
        already called.*
        
        Args:
            self (none): None.
        Returns:
            (List): Contains Product Items in a List.
        """
        return self._list_of_ProductItems

    def get_cart_json(self):
        """
        Public Accessor for the Member Variable: Cart_Json - JSON Object.
        
        Args:
            self (none): None.
        Returns:
            (JSON Object): JSON Object Represented in the Cart JSON 
            File.
        """
        return self._cart_json