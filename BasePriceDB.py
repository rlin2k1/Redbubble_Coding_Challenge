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
from Cart import Cart

class BasePriceDB:
    """
    BasePriceDB Class - Represents a Database Price Point for Product Items.
    
    Attributes:
        _cart (Cart Object): Cart Object Representing a Shopping Cart Containing
            Product Items.
        _price_json (JSON Object): JSON Object Represented in the Base Price
        JSON File.
        _discount_json (JSON Object): JSON Object Represented in the Discounts
        JSON File.
        _price_count (Integer): The Count of different items in Base Prices
    """
    def __init__(self, price_json, discount_json, cart):
        """
        Constructor for the BasePriceDB Class.
        
        Args:
            self (none): None.
            price_json (JSON Object): JSON Object Represented in the Base Price
            JSON File.
            discount_json (JSON Object): JSON Object Represented in the Discounts
            JSON File.
            cart (Cart Object): Cart Object Representing a Shopping Cart Containing
            Product Items.
        Returns:
            (void): No return value. Just sets member variables.
        """
        self._cart = cart
        self._price_json = price_json
        self._price_count = self.calculate_price_count(price_json)
        self._discount_json = discount_json

    def calculate_price_count(self, price_json):
        """
        Calculates How Many Different Items there Are in the Base Prices.
        
        Args:
            self (none): None.
            price_json (JSON Object): JSON Object Represented in the Base Price
            JSON File.
        Returns:
            (Integer): Count of Different Items in Base Prices.
        """
        count = 0
        for price_item in price_json:
            count = count + 1
        return count

    def get_price_count(self):
        """
        Public Accessor for the Member Variable: Price Count - Integer.
        *More Memory Efficient for BasePriceDB if calculate_price_count()
        was already called.*
        
        Args:
            self (none): None.
        Returns:
            (Integer): Count of Different Items in Base Prices.
        """
        return self._price_count
    
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

        price = (base_price + round(base_price * product.get_artist_markup()\
        / 100) ) * product.get_quantity()

        #Check if the Quantity of the Product Meets the Discount Threshold
        #If so, Update Price
        product_quant_dict = self._cart.get_product_quant_dict()
        product_type = product.get_product_type()

        final_quantity = product_quant_dict[product_type] #NEED TO GET FROM CART DICTIONARY -> From Product Type

        optimal_threshold = -1
        optimal_percentage = -1

        for product_d in self._discount_json:
            if product_type == product_d['product-type']:
                discounts = product_d['discounts']
                for discount in discounts:
                    if final_quantity >= discount['threshold'] and discount['threshold'] > optimal_threshold:
                        optimal_threshold = discount['threshold']
                        optimal_percentage = discount['percent'] #NEED TO KEEP PERCENTAGE

        if(optimal_threshold != -1 and optimal_percentage != -1):
            price = round(price * (100.0 - optimal_percentage) / 100)

        return int(price)
