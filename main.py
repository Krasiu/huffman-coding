from collections import Counter

from huffman import create_hoffman_tree, encode_text, decode_text


def run_sample():
    with open("sample_text.txt") as f:
        sample_text = f.read()

    frequencies = Counter(sample_text).most_common()
    tree = create_hoffman_tree(frequencies)
    encoded = encode_text(sample_text, tree)
    decoded = decode_text(encoded, tree)

    length_before = len(sample_text) * 8
    length_after = len(decoded) * 8
    length_encoded = len(encoded)

    print(f"Size matches: {length_before == length_after}")
    print(f"Coefficient: {length_encoded/length_after}")


if __name__ == '__main__':
    run_sample()
