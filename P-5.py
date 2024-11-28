import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]

def generate_codes(node, current_code="", codes={}):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encoding(word, codes):
    encoded_text = ""
    for char in word:
        if char in codes:
            encoded_text += codes[char]
        else:
            return "illegal character"
    return encoded_text

def calculate_compression_ratio(original_text, encoded_text):
    original_bits = len(original_text) * 8
    encoded_bits = len(encoded_text)
    return (1 - (encoded_bits / original_bits)) * 100

frequencies = {
    'k': 10, 'o': 5, 'r': 2, 'e': 15, 
    'a': 18, 't': 4, 'c': 7, 'h': 11
}

huffman_tree = build_huffman_tree(frequencies)
huffman_codes = generate_codes(huffman_tree)

while True:
    word = input("Please a word: ").strip()
    encoded_result = huffman_encoding(word, huffman_codes)

    if encoded_result == "illegal character":
        print("illegal character")
        continue

    original_size = len(word) * 8
    encoded_size = len(encoded_result)

    print(f"결과 비트 열: {encoded_result}")
    print(f"압축률: {calculate_compression_ratio(word, encoded_result):.2f}%")
    break
