# Function to solve 0/1 knapsack problem using dynamic programming
def knapsack_dp(capacity, weights, values, n):
    # Create a 2D DP array to store the maximum value for each subproblem
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the DP table in a bottom-up manner
    for i in range(1, n + 1):  # Iterate over items
        for w in range(1, capacity + 1):  # Iterate over each possible capacity
            if weights[i - 1] <= w:  # If the item can be included
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:  # If the item cannot be included
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]  # Return the maximum value for full capacity

# User input for items and knapsack capacity
if __name__ == "__main__":
    # Input number of items
    n = int(input("Enter the number of items: "))

    # Lists to store the weights and values of each item
    values = []
    weights = []
    
    # Input the values and weights for each item
    for i in range(n):
        value = int(input(f"Enter the value of item {i + 1}: "))
        weight = int(input(f"Enter the weight of item {i + 1}: "))
        values.append(value)
        weights.append(weight)
    
    # Input the knapsack capacity
    knapsack_capacity = int(input("Enter the knapsack capacity: "))
    
    # Call the knapsack function and print the result
    max_value = knapsack_dp(knapsack_capacity, weights, values, n)
    print(f"Maximum value in knapsack = {max_value}")
