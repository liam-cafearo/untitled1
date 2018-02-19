from decimal import Decimal
"""
Import decimal module to deal with floating point issues.
"""
coins = [1, .50, .20, .10, .05, .02, .01]

available_items = {
    'coke': .73,
    'biscuits': 1.15,
    'apple': .43
}

# available items is a dictionary of items with their cost


def give_change(amount):
    change = []
    amount = Decimal(str(amount))
    """
    We convert amount into a string then a Decimal
    """
    for coin in coins:
        coin = Decimal(str(coin))
        """
        We convert coin into a string, then a Decimal
        """
        while coin <= amount:
            amount -= coin
            change.append(float(coin))
            """
            We've to turn each coin back into a float, otherwise the list of coins would look like this:
            [Decimal('0.1'), Decimal('0.5'), Decimal('0.2') and the tests would fail.
            """
    return change


def give_item_and_change(item, amount):
    if item not in available_items:
        return None, amount, "that item isn't available"

    cost = available_items[item]

    if amount < cost:
        return None, amount, 'not enough money'

    change_to_return = amount - cost
    coins = give_change(change_to_return)
    return item, coins, "here's your change"


if __name__ == '__main__':
    """
    This is to stop the code below running when we import the program into our test class.
    If it's not there, the code will run and stop the tests running.
    Essentially if __name__ == '__main__' means 'if this program is actually being run, not just imported'.
    """
    while True:
        item = raw_input('choose item: %s' % available_items)
        amount = input('enter amount in pounds:')
        print give_item_and_change(item, amount)
