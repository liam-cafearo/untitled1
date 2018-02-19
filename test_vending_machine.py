import unittest
from vending_machine import give_change
from vending_machine import give_item_and_change


class TestVendingMachine(unittest.TestCase):
    """
    Define a class that inherits from unittest.TestCase which is the unit
    testing model that ships with python.
    """
    def test_return_change(self):
        """
        Method name has to start with test_ in order for it to run.
        Because we inherited from unittest.TestCase,
        we have some useful methods that we can use, such as assertEqual
        """
        self.assertEqual(give_change(.17), [.10, .05, .02], 'wrong change given')
        self.assertEqual(give_change(.18), [.10, .05, .02, .01], 'wrong change given')

    def test_multiple_same_coins(self):
        """
        test if change can be given in multiples of a coin
        """
        self.assertEqual(give_change(.04), [.02, .02])

    def test_unavailable_item(self):
        """if user asks for an item that's unavailable, they should not be given the item,
        and their money should be returned"""
        item, change, _ = give_item_and_change('crisps', .50)
        # the use of the _ is a convention to denote a throwaway
        # variable name that is being deliberately ignored.
        self.assertIsNone(item)
        # we use assertIsNone but we could have used assertEqual(item, None)
        self.assertEqual(change, .50)

    def test_not_enough_money(self):
        """
        if user asks for an item but pays too little,
        they should not be given the item,
        and their money should be returned
        """
        item, change, _ = give_item_and_change('coke', .50)
        self.assertIsNone(item)
        self.assertEqual(change, .50)

    def test_correct_change(self):
        """
        if user asks for an item and pays too much
        they should get the correct change .
        """
        item, change, _ = give_item_and_change('coke', 1.00)
        self.assertEqual(change, [.20, .05, .02])
