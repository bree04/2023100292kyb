import heapq
from collections import defaultdict

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(freq, char) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes(node, prefix="", codebook={}):
    if node is None:
        return
    if node.char is not None:
        codebook[node.char] = prefix
    build_codes(node.left, prefix + "0", codebook)
    build_codes(node.right, prefix + "1", codebook)
    return codebook

def calculate_compression_ratio(original_text, encoded_text):
    original_bits = len(original_text) * 8
    encoded_bits = len(encoded_text)
    compression_ratio = (original_bits - encoded_bits) / original_bits * 100
    return compression_ratio

def huffman_encoding():
    frequencies = {}
    
    
    target_chars = input("코딩 대상 문자: ").strip()
    
    
    print("각 문자의 빈도수.")
    for char in target_chars:
        if char in frequencies:
            continue  
        freq = int(input(f"'{char}'의 빈도수: ").strip())
        frequencies[char] = freq

    if not frequencies:
        print("빈도 없음.")
        return

    huffman_tree = build_huffman_tree(frequencies)
    codebook = build_codes(huffman_tree)

    while True:
        text = input("Please enter a word: ")
        if not all(char in codebook for char in text):
            print("illegal character")
            continue

        encoded_text = ''.join(codebook[char] for char in text)
        print("결과 비트열:", encoded_text)
        compression_ratio = calculate_compression_ratio(text, encoded_text)
        print("압축률:", compression_ratio, "%")
        break

if __name__ == "__main__":
    huffman_encoding()
