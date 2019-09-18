# Initializing our blockchain List
blockchian = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain"""
    return blockchian[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain"""
    blockchian.append([last_transaction, transaction_amount])


def get_user_input():
    return float(input('Your Transaction amount Please'))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(),
          transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchian)


"""
The output is:-
 [[[1], 56.0], [[[1], 56.0], 78.0], [[[[1], 56.0], 78.0], 90.0]]
 
"""
