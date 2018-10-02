""" BasePriceDB.py
This module contains the BasePriceDB Class.

Author(s):
    Redbubble Applicant

Date Created:
    October 2nd, 2018
"""
# ---------------------------------------------------------------------------- #
# Import Statements for the Necessary Packages / Modules
# ---------------------------------------------------------------------------- #
from ProductItem import ProductItem

class BasePriceDB:
    """
    BasePriceDB Class - Represents a Database Price Point for Product Items.
    
    Attributes:
        _price_json (JSON Object): JSON Object Represented in the Base Price
        JSON File.
    """
    def __init__(self, price_json):
        """
        Constructor for the BasePriceDB Class.
        
        Args:
            self (none): None.
            price_json (JSON Object): JSON Object Represented in the Base Price
            JSON File.
        Returns:
            (void): No return value. Just sets member variables.
        """
        self._price_json = price_json
    
    def get_price_json(self):
        """
        Public Accessor for the Member Variable: Price_Json - JSON Object.
        
        Args:
            self (none): None.
        Returns:
            (JSON Object): JSON Object Represented in the Base Price JSON 
            File.
        """
        return self._price_json

    def get_price_point(self, product):
        """
        Returns the Price of a ProductItem in relation to the ProductItem's
        attributes.
        
        Args:
            self (none): None.
            product (ProductItem): Represents a Product Item in the Redbubble
            Shopping Cart.
        Returns:
            (Integer): The Price of the Product in Cents. Sentinel: Returns -1 
            if ERROR and Price Cannot Be Found.
        """
        base_price = -1
        
        for price in self._price_json:
            if product.get_product_type() == price['product-type']:
                #We MAY Have a Match - Need to Check If Options Are the Same
                match = True #Sentinel Flag Check. Innocent until proven guilty!
                product_options = product.get_options()
                price_options = price['options']
                for option in price_options:
                    if(product_options[option] not in price_options[option]):
                        match = False
                        break
                if(match):
                    base_price = price['base-price']
                    break

        price = base_price + round(base_price * product.get_artist_markup()\
        / 100) * product.get_quantity()

        return int(price)