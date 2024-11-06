import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_map = defaultdict(int)
    for char in text:
        freq_map[char] += 1
    priority_queue = []
    for char, freq in freq_map.items():
        heapq.heappush(priority_queue, Node(char, freq))

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def generate_huffman_code(root, prefix="", codebook = None):
    if codebook is None:
        codebook = {}

    if root is not None:
        if root.char is not None:
            codebook[root.char] = prefix
        generate_huffman_code(root.left, prefix + "0", codebook)
        generate_huffman_code(root.right, prefix + "1", codebook)

    return codebook

def huffman_encoding(text):
    root = build_huffman_tree(text)
    huffman_code = generate_huffman_code(root)
    encoded_text = ''.join(huffman_code[char] for char in text)
    return encoded_text, huffman_code

def huffman_decoding(encoded_text, huffman_codes):
    # Reverse the Huffman codes to map binary codes to characters
    reverse_codes = {v: k for k, v in huffman_codes.items()}

    # Decode the encoded text
    current_code = ""
    decoded_text = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""

    return decoded_text

text = "this is an example for huffman encoding"
encoded_text, huffman_code = huffman_encoding(text)
print(encoded_text)
print(huffman_decoding(encoded_text, huffman_code))