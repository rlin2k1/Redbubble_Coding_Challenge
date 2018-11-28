""" automated_tests.py
Automated Tests for the Redbubble Summer 2019 Internship Coding Challenge
DO NOT FORGET EDGE CASES!
    -What if 0?
    -What if Order Just Leggings? (No Options!)
    -What if Repeated Item in Cart with Separate Quanities?

Author(s):
    Roy Lin

Date Created:
    October 2nd, 2018
"""
# ---------------------------------------------------------------------------- #
# Import Statements for the Necessary Packages / Modules
# ---------------------------------------------------------------------------- #
from __future__ import print_function #Make Print Compatible with Python 2 and 3
import json #To Parse Through JSON Files
import unittest #For Automated Testing Purposes

from Cart import Cart #For Cart Class Containing Items
from BasePriceDB import BasePriceDB #For Base Price Class DataBase Creation
from PriceCalculator import PriceCalculator #Price Calculator Class - Find Price
from calculate_the_price import return_json_data

# ---------------------------------------------------------------------------- #
# Initialization of Testing Variables - Easily Extendible and Dynamic!
# ---------------------------------------------------------------------------- #
list_of_cart_jsons = ['./Test_Files/Test_Carts/cart-4560.json', \
'./Test_Files/Test_Carts/cart-9363.json', \
'./Test_Files/Test_Carts/cart-9500.json', \
'./Test_Files/Test_Carts/cart-11356.json', \
'./Test_Files/Test_Carts/cart-0.json', \
'./Test_Files/Test_Carts/cart-no-options-leggings.json', \
'./Test_Files/Test_Carts/cart-repeat-item-quantity.json']

list_of_price_jsons = ['./Test_Files/Test_Base_Prices/base-prices.json']

list_of_checkout_prices = [4560, 9363, 9500, 11356, 0, 19500, 9120]

list_of_cart_item_count = [1, 2, 2, 1, 0, 1, 2]

list_of_price_item_count = [10]

list_of_mark_up_prices = [4560, 9120, 243, 4560, 4940, 11356 ,19500, 4560, 4560]

class TestPriceCalculator(unittest.TestCase):
    def test_cart_prices_json(self):
        print()
        print("Following Tests tested with Base Price File: " + \
        list_of_price_jsons[0] + ":")
        print()
        for i in range(0, len(list_of_cart_jsons)):
            print("Testing Cart JSON File: " + list_of_cart_jsons[i] + \
            " with Expected Cart Value of " + str(list_of_checkout_prices[i]))

            #Testing Base - calculate_the_price.py
            cart_json = return_json_data(list_of_cart_jsons[i])
            price_json = return_json_data(list_of_price_jsons[0])
            rb_cart = Cart(cart_json)
            base_price_db = BasePriceDB(price_json)
            price_calculator = PriceCalculator(rb_cart, base_price_db)
            actual_cart_value = price_calculator.get_price_cents()
            print("Actual Cart Value: " + \
            str(price_calculator.get_price_cents()), end = '')

            self.assertEqual(actual_cart_value, list_of_checkout_prices[i])
            print(" - PASS")
            print()
        print("----------------------------------------------------------------\
-------")

    def test_cart_item_count(self):
        for i in range(0, len(list_of_cart_jsons)):
            print("Testing Cart JSON File: " + list_of_cart_jsons[i] + \
            " with Expected Cart Item Amount of " + \
            str(list_of_cart_item_count[i]))

            #Testing Cart Class
            cart_json = return_json_data(list_of_cart_jsons[i])
            rb_cart = Cart(cart_json)
            actual_cart_item_amount = len(rb_cart.get_product_items())
            print("Actual Cart Item Amount: " + str(actual_cart_item_amount), \
            end = "")

            self.assertEqual(actual_cart_item_amount, \
            list_of_cart_item_count[i])
            print(" - PASS")
            print()
        print("----------------------------------------------------------------\
-------")

    def test_price_item_count(self):
        print()
        for i in range(0, len(list_of_price_jsons)):
            print("Testing Price JSON File: " + list_of_price_jsons[i] + \
            " with Expected Item Amount of " + \
            str(list_of_price_item_count[i]))

            #Testing BasePriceDB Class
            price_json = return_json_data(list_of_price_jsons[i])
            base_price_db = BasePriceDB(price_json)
            actual_price_item_amount = base_price_db.get_price_count()
            print("Actual Item Amount: " + str(actual_price_item_amount), \
            end = "")

            self.assertEqual(actual_price_item_amount, \
            list_of_price_item_count[i])
            print(" - PASS")
            print()
        print("----------------------------------------------------------------\
-------")

    def test_mark_up_prices(self):
        print()
        mark_up_prices_index = 0
        for i in range(0, len(list_of_cart_jsons)):
            print("Testing Cart JSON File: " + list_of_cart_jsons[i])

            #Testing Cart and BasePriceDB Class
            cart_json = return_json_data(list_of_cart_jsons[i])
            rb_cart = Cart(cart_json)
            price_json = return_json_data(list_of_price_jsons[0])
            base_price_db = BasePriceDB(price_json)

            list_of_cart_items = rb_cart.get_product_items()

            for product in list_of_cart_items:
                print("Type - " + product.get_product_type())
                print("With Options - " + str(json.dumps(product.get_options())))
                print("With Artist Markup - " + str(product.get_artist_markup()))
                print("With Quantitiy - " + str(product.get_quantity()))
                print("Expected Final Price is:" +  str(list_of_mark_up_prices[mark_up_prices_index]))
                print("Actual Final Price: " + \
                str(base_price_db.get_price_point(product)), end = "")
                self.assertEqual(base_price_db.get_price_point(product),\
            list_of_mark_up_prices[mark_up_prices_index])
                mark_up_prices_index = mark_up_prices_index + 1
                print(" - PASS")
                print()
            print(list_of_cart_jsons[i] + " = PASS")
            print()
        print("----------------------------------------------------------------\
-------")

if __name__ == '__main__':
    unittest.main()
