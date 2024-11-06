import heapq

# Class to represent a node in the Huffman Tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq           # Frequency of the character
        self.symbol = symbol       # Character
        self.left = left           # Left child
        self.right = right         # Right child
        self.huff = ""             # Huffman code for the node

    # Comparator function to make the Node class compatible with heapq
    def __lt__(self, other):
        return self.freq < other.freq

# Recursive function to print Huffman codes of each character
def printNodes(node, val=""):
    newval = val + node.huff

    # If node is a leaf node, print its symbol and Huffman code
    if node.left is None and node.right is None:
        print(f"{node.symbol} -> {newval}")
    else:
        # Traverse left and right children
        if node.left:
            printNodes(node.left, newval)
        if node.right:
            printNodes(node.right, newval)

# Main function
if __name__ == "__main__":
    # Taking input for characters and their frequencies
    n = int(input("Enter the number of characters: "))
    chars = []
    freqs = []

    for i in range(n):
        char = input(f"Enter character {i + 1}: ")
        freq = int(input(f"Enter frequency of {char}: "))
        chars.append(char)
        freqs.append(freq)

    # Create a priority queue (min-heap) to store nodes of the Huffman tree
    nodes = []

    # Add all characters with their frequencies as nodes in the min-heap
    for i in range(len(chars)):
        heapq.heappush(nodes, Node(freqs[i], chars[i]))

    # Build the Huffman tree
    while len(nodes) > 1:
        # Extract two nodes with the lowest frequencies
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        # Assign '0' to left child and '1' to right child
        left.huff = "0"
        right.huff = "1"

        # Create a new internal node with frequency equal to the sum of the two nodes
        newnode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        # Add the new node back to the heap
        heapq.heappush(nodes, newnode)

    # Print the Huffman codes by traversing the Huffman tree
    print("\nHuffman Codes:")
    printNodes(nodes[0])
