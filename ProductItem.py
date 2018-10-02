""" ProductItem.py
This module contains the ProductItem Class.

Author(s):
    Redbubble Applicant

Date Created:
    October 2nd, 2018
"""
class ProductItem:
    """
    ProductItem Class - Represents a Product Item in the Redbubble Shopping 
    Cart.
    
    Attributes:
        _product_type (String): The Type of the Product Being Purchased.
        _options (Key-value pairs of strings.): Options that the Product Item
        Falls Under.
        _artist_markup (Integer): The artist markup in percent, for example 20 
        represents a 20% markup.
        _quantity (Integer): The quantity of this item.
    
    """
    def __init__(self, product_type, options, artist_markup, quantity):
        """
        Constructor for the ProductItem Class.
        
        Args:
            self (none): None.
            product_type (String): The Type of the Product Being Purchased.
            options (Key-value pairs of strings.): Options that the Product Item
            Falls Under.
            artist_markup (Integer): The artist markup in percent, for example 20 
            represents a 20% markup.
            quantity (Integer): The quantity of this item.
        
        Returns:
            (void): No return value. Just sets member variables.
        """
        self._product_type = product_type
        self._options = options
        self._artist_markup = artist_markup
        self._quantity = quantity

    def get_product_type(self):
        """
        Public Accessor for the Member Variable: Product Type.
        
        Args:
            self (none): None.
        Returns:
            (String): The Type of the Product Being Purchased.
        """
        return self._product_type
    
    def get_options(self):
        """
        Public Accessor for the Member Variable: Options.
        
        Args:
            self (none): None.
        Returns:
            (Key-value pairs of strings.): Options that the Product Item Falls 
            Under.
        """
        return self._options

    def get_artist_markup(self):
        """
        Public Accessor for the Member Variable: Artist Markup.
        
        Args:
            self (none): None.
        Returns:
            (Integer): The artist markup in percent, for example 20 represents a
            20% markup.
        """
        return self._artist_markup

    def get_quantity(self):
        """
        Public Accessor for the Member Variable: Quantity.
        
        Args:
            self (none): None.
        Returns:
            (Integer): The quantity of this item.
        """
        return self._quantity