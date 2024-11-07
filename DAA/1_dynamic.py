# Function to solve 0/1 Knapsack problem using dynamic programming
def knapsack_01(weights, values, capacity):
    n = len(values)  # Number of items

    # Initialize a DP table with all values set to 0
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Option 1: Include the item
                include_item = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                # Option 2: Exclude the item
                exclude_item = dp[i - 1][w]
                # Take the maximum of including or excluding the item
                dp[i][w] = max(include_item, exclude_item)
            else:
                # If the item's weight is more than the current capacity, exclude it
                dp[i][w] = dp[i - 1][w]

    # The maximum value will be in the bottom-right corner of the DP table
    return dp[n][capacity]

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

max_value = knapsack_01(weights, values, capacity)
print(f"Maximum value achievable in the knapsack: {max_value}")
