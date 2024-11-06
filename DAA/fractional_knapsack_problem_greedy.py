class Item:

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def value_weight_ratio(self):
        return self.value/self.weight

def fractional_kanpsack_problem(items, capacity):
    items.sort(key = lambda x : x.value_weight_ratio(), reverse=True)
    total_value = 0
    for item in items:
        if capacity > 0:
            if item.weight <= capacity:
                total_value += item.value
                capacity -= item.weight
            else:
                fraction = capacity/item.weight
                total_value += item.value * fraction
                capacity = 0
        else:
            break

    return total_value

items = [
    Item(60, 10),  # Item with value 60 and weight 10
    Item(100, 20), # Item with value 100 and weight 20
    Item(120, 30)  # Item with value 120 and weight 30
]
capacity = 50  # Total weight capacity of the knapsack

max_value = fractional_kanpsack_problem(items, capacity)
print(f"Maximum value achievable in the knapsack: {max_value}")