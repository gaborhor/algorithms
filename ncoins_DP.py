# Below are two algorithms (Divide-And-Conquer and Dynamic Programming) to compute the
# minimum number of coins required to produce a cent's worth of change.
# The DP version also prints out the coins needed to produce this minimum

from time import time

# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0: # Base case
        return 0
    else: # Recursive case
        minCoins = float("inf")
        for currentCoin in coins: # Check all coins
            # If we can provide change
            if (amount - currentCoin) >= 0:
                # Calculate optimal for currentCoin
                currentMin = DACcoins(coins, amount-currentCoin) + 1
                # Keep the best number of coins
                minCoins = min(minCoins, currentMin)
        return minCoins


# Algorithm 2: Dynamic Programming w/ Traceback
def DPcoins(coins, amount):
    # Create initial tables
    min_coins = [float('inf') for i in range(amount+1)] # Initialize placeholders up to the number of the money amount
    traceback = [0 for i in range(amount+1)]

    # Fill in the base case(s)
    min_coins[0] = 0    # Zero money gets zero change coins

    # Fill in the rest of the table
    for new_amount in range(1, amount+1):   # For each money value up to amount input
        for coin in coins:                  # And for each value of coin we can use to provide change
            # If the coin can be subtracted from the money amount, and if this actually reduces the number of coins used
            if (new_amount - coin) >= 0 and min_coins[new_amount] > min_coins[new_amount - coin] + 1:
                # Increase the number of coins used at the "current use location" by 1, relative to the "old use location"
                min_coins[new_amount] = min_coins[new_amount - coin] + 1
                # Record the value of the current coin for traceback
                traceback[new_amount] = coin

    # Perform the traceback to print result
    sum_of_money = amount
    while sum_of_money > 0:
        print(traceback[sum_of_money])          # Display the current coin value at this money value
        sum_of_money -= traceback[sum_of_money] # and subtract the coin value from the money value

    print(min_coins)
    print(traceback)
    return min_coins[amount] # return optimal number of coins

# Testing code
C = [1,5,10,12,25] # coin denominations (must include a penny)
A = int(input('Enter desired amount of change: '))
assert A>=0
print("DAC:")
t1 = time()
numCoins = DACcoins(C,A)
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")
print()
print("DP:")
t1 = time()
numCoins = DPcoins(C,A)
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")