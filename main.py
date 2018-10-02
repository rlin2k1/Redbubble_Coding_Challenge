""" main.py
http://take-home-test.herokuapp.com/new-product-engineer
Price Calculator Command-Line Program - Outputs the Total Price in the User's
Shopping Cart in Cents

USAGE: python3 -c /PATHTOCARTJSON -p /PATHTOBASEPRICE

Author(s):
    Redbubble Applicant

Date Created:
    October 1st, 2018
"""
# ---------------------------------------------------------------------------- #
# Import Statements for the Necessary Packages
# ---------------------------------------------------------------------------- #
import argparse #For Argument Parsing
import json #For JSON Parsing

def main():
    # ------------------------------------------------------------------------ #
    # Constructs Argument Parser for Parsing Arguments
    # ------------------------------------------------------------------------ #
    argument_parser = argparse.ArgumentParser(description='Price Calculator')
    argument_parser.add_argument("-c", "--cart", required=True, \
    help="PATH TO CART JSON")
    argument_parser.add_argument("-p", "--price", required=True, \
    help="PATH TO BASE PRICE JSON")

    arguments = vars(argument_parser.parse_args())
    # ------------------------------------------------------------------------ #
    # Get JSON Paths for Cart and Base Prices
    # ------------------------------------------------------------------------ #
    path_to_cart = arguments['cart']
    path_to_price = arguments['price']

    

if __name__ == '__main__':
    main()