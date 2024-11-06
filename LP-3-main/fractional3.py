# Class to represent an item with value and weight
class Item:
    def __init__(self, value, weight):
        self.value = value      # Value of the item
        self.weight = weight    # Weight of the item

    # Function to calculate value-to-weight ratio
    def value_weight_ratio(self):
        return self.value / self.weight

# Function to solve fractional knapsack problem
def fractional_knapsack(capacity, items):
    # Sort items based on value-to-weight ratio in descending order
    items.sort(key=lambda x: x.value_weight_ratio(), reverse=True)
    
    total_value = 0.0  # Total value in knapsack
    
    for item in items:
        if capacity >= item.weight:
            # Take the whole item
            capacity -= item.weight
            total_value += item.value
            print(f"Took whole item with value {item.value} and weight {item.weight}")
        else:
            # Take fraction of the item
            fraction = capacity / item.weight
            total_value += item.value * fraction
            print(f"Took {fraction * 100:.2f}% of item with value {item.value} and weight {item.weight}")
            capacity = 0
            break
    
    return total_value

# User input for items and knapsack capacity
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    items = []
    
    for i in range(n):
        value = float(input(f"Enter value of item {i + 1}: "))
        weight = float(input(f"Enter weight of item {i + 1}: "))
        items.append(Item(value, weight))
    
    knapsack_capacity = float(input("Enter the knapsack capacity: "))
    
    max_value = fractional_knapsack(knapsack_capacity, items)
    print(f"Maximum value in knapsack = {max_value}")
