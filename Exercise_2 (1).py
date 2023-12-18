class BinaryHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.heapify_up(self.size - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[i][0] < self.heap[self.parent(i)][0]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_min(self):
        if self.size == 0:
            return None

        min_value = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        del self.heap[self.size]
        self.heapify_down(0)
        return min_value

    def heapify_down(self, i):
        while True:
            smallest = i
            left = self.left_child(i)
            right = self.right_child(i)

            if left < self.size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left

            if right < self.size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest


class PriorityQueue:
    def __init__(self):
        self.binary_heap = BinaryHeap()

    def insert(self, value):
        self.binary_heap.insert(value)

    def extract_min(self):
        return self.binary_heap.extract_min()

    def is_empty(self):
        return self.binary_heap.size == 0


class HuffmanNode:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None


def build_huffman_tree(string):
    frequency_map = {}
    for char in string:
        if char in frequency_map:
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1

    priority_queue = PriorityQueue()
    for symbol, frequency in frequency_map.items():
        node = HuffmanNode(symbol, frequency)
        priority_queue.insert((frequency, node))

    while not priority_queue.is_empty() and priority_queue.binary_heap.size > 1:
        freq1, left_node = priority_queue.extract_min()
        freq2, right_node = priority_queue.extract_min()

        new_node = HuffmanNode(None, freq1 + freq2)
        new_node.left = left_node
        new_node.right = right_node

        priority_queue.insert((new_node.frequency, new_node))

    _, root = priority_queue.extract_min()
    return root


def generate_huffman_codes(root):
    codes = {}

    def traverse(node, code):
        if node.symbol is not None:
            codes[node.symbol] = code
            return

        traverse(node.left, code + '0')
        traverse(node.right, code + '1')

    traverse(root, '')
    return codes


def encode_string(string, codes):
    encoded_string = ''
    for char in string:
        encoded_string += codes[char]
    return encoded_string


# Test the implementation
input_string = "I love data structures"
huffman_tree = build_huffman_tree(input_string)
huffman_codes = generate_huffman_codes(huffman_tree)
encoded_string = encode_string(input_string, huffman_codes)

print("Encoded:", encoded_string)
print("Huffman Codes:")
for symbol, code in huffman_codes.items():
    print(symbol, ":", code)

compression_ratio = (len(encoded_string) / (8 * len(input_string))) * 100
print("Compression Ratio: {:.2f}%".format(compression_ratio))