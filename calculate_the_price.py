""" calculate_the_price.py
http://take-home-test.herokuapp.com/new-product-engineer
Price Calculator Command-Line Program - Outputs the Total Price in the User's
Shopping Cart in Cents.

USAGE: python3 calculate_the_price -c /PATHTOCARTJSON -p /PATHTOBASEPRICEJSON -d /PATHTODISCOUNTJSON

Author(s):
    Redbubble Applicant

Date Created:
    October 1st, 2018
"""
# ---------------------------------------------------------------------------- #
# Import Statements for the Necessary Packages / Modules
# ---------------------------------------------------------------------------- #
import argparse #For Argument Parsing
import json #For JSON Parsing

from Cart import Cart #For Cart Class Containing Items
from BasePriceDB import BasePriceDB #For Base Price Class DataBase Creation
from PriceCalculator import PriceCalculator #Price Calculator Class - Find Price
# ---------------------------------------------------------------------------- #
# Helper Functions for Price Calculator
# ---------------------------------------------------------------------------- #
def return_json_data(path_to_file):
    """
    Returns the JSON Object for Use with Python's JSON Library.
    
    Args:
        path_to_file (String): File Path to JSON File.
    Returns:
        (JSON Object): JSON Object Represented in the JSON File.
    """
    try:
        opened_file = open(path_to_file, 'r')
        json_object = json.load(opened_file)
        return json_object
    except:
        print("Cannot Open the Path to " + path_to_file)
        exit(1)

def main():
    """
    main Function for the Redbubble Coding Challenge of Calculating the Price
    in the Redbubble Shopping Cart in terms of Cents.
    
    Args:
        self (none): None.
    Returns:
        (void): No return value. Just prints the Total Price in the Cart
        in Cents
    """
    # ------------------------------------------------------------------------ #
    # Constructs Argument Parser for Parsing Arguments
    # ------------------------------------------------------------------------ #
    argument_parser = argparse.ArgumentParser(description='Price Calculator')
    argument_parser.add_argument("-c", "--cart", required=True, \
    help="PATH TO CART JSON")
    argument_parser.add_argument("-p", "--price", required=True, \
    help="PATH TO BASE PRICE JSON")
    argument_parser.add_argument("-d", "--discount", required=True, \
    help="PATH TO DISCOUNT JSON")

    arguments = vars(argument_parser.parse_args())

    # ------------------------------------------------------------------------ #
    # Get and Load JSON Paths for Cart, Base Prices, and Discounts
    # ------------------------------------------------------------------------ #
    path_to_cart = arguments['cart']
    path_to_price = arguments['price']
    path_to_discount = arguments['discount']

    cart_json = return_json_data(path_to_cart)
    price_json = return_json_data(path_to_price)
    discount_json = return_json_data(path_to_discount)

    # ------------------------------------------------------------------------ #
    # Initialize Cart with Each Item
    # ------------------------------------------------------------------------ #
    rb_cart = Cart(cart_json)

    # ------------------------------------------------------------------------ #
    # Initialize Base Price DataBase with Cart and Discount
    # ------------------------------------------------------------------------ #
    base_price_db = BasePriceDB(price_json, discount_json, rb_cart)

    # ------------------------------------------------------------------------ #
    # Initialize Price Calculator
    # ------------------------------------------------------------------------ #
    price_calculator = PriceCalculator(rb_cart, base_price_db)

    # ------------------------------------------------------------------------ #
    # Output Price of Shopping Cart Compared to Base Prices
    # ------------------------------------------------------------------------ #
    print(price_calculator.get_price_cents())
    return

if __name__ == '__main__':
    main()
