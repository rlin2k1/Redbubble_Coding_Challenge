""" PriceCalculator.py
This module contains the PriceCalculator Class.

Author(s):
    Redbubble Applicant

Date Created:
    October 2nd, 2018
"""
# ---------------------------------------------------------------------------- #
# Import Statements for the Necessary Packages / Modules
# ---------------------------------------------------------------------------- #
from Cart import Cart
from BasePriceDB import BasePriceDB

class PriceCalculator:
    """
    PriceCalculator Class - Calculator for Product Items in the RedBubble
    Shopping Cart.
    
    Attributes:
        _price_in_cart_cents (Integer): Represents the Price in the RedBubble
        Shopping Cart in Cents.
        *(Can Be Easily Extendible for Other Features as Well)*
    """
    def __init__(self, cart, base_price_db):
        """
        Constructor for the PriceCalculator Class.
        
        Args:
            self (none): None.
            cart (Cart): Cart Object Representing a List of ProductItems.
            base_price_db (BasePriceDB): BasePriceDB Object Containing the
            Base Prices of current Redbubble Offerings.
        Returns:
            (void): No return value. Just sets member variables.
        """
        self._price_in_cart_cents = self.calculate_cart_price_cents(cart, \
        base_price_db)

    def calculate_cart_price_cents(self, cart, base_price_db):
        """
        Calculates the Total Price of the Cart in Cents.
        
        Args:
            self (none): None.
            cart (Cart): Cart Object Representing a List of ProductItems.
            base_price_db (BasePriceDB): BasePriceDB Object Containing the
            Base Prices of current Redbubble Offerings.
        Returns:
            (Integer): The Total Price of the Cart in Cents.
        """
        running_total = 0
        product_items = cart.get_product_items()
        for product in product_items:
            running_total = running_total + \
            base_price_db.get_price_point(product)
        return running_total

    def get_price_cents(self):
        """
        Public Accessor for the Member Variable: Price in Cart (Cents).
        *More Memory Efficient for Product Items if calculate_cart_price_cents()
        was already called.*
        
        Args:
            self (none): None.
        Returns:
            (Integer): The Total Price of the Cart in Cents.
        """
        return self._price_in_cart_cents