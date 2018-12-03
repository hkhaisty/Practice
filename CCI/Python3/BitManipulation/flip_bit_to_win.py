import unittest


def get_binary_sequences(number):
    sequences = []
    bit = count = 0
    while number != 0:
        if (number & 1) != bit:
            sequences.append(count)
            bit = number & 1
            count = 0
        count += 1
        number >>= 1

        if number == 0:
            sequences.append(count)

    return sequences


def find_longest_sequence(sequences):
    max_sequence = 0
    for i in range(0, len(sequences), 2):
        left_sequence = sequences[i-1] if i > 0 else 0
        right_sequence = sequences[i+1] if i < len(sequences) + 1 else 0
        if sequences[i] == 1:
            sequence = 1 + left_sequence + right_sequence
        elif sequences[i] > 1:
            sequence = 1 + max(left_sequence, right_sequence)
        else:
            sequence = max(left_sequence, right_sequence)

        max_sequence = max(max_sequence, sequence)

    return max_sequence


def flip_bit_to_win(number):
    return find_longest_sequence(get_binary_sequences(number))


def flip_bit_optimal(number):
    curr_length = prev_length = 0
    max_length = 0
    while number != 0:
        if (number & 1) == 1:
            curr_length += 1
        elif (number & 1) == 0:
            prev_length = 0 if (number & 2) == 0 else curr_length
            curr_length = 0
        max_length = max(prev_length + curr_length + 1, max_length)
        number >>= 1

    return max_length


class Test(unittest.TestCase):
    def test_flip_bit_to_win(self):
        self.assertEqual(2, flip_bit_optimal(9))
        self.assertEqual(8, flip_bit_to_win(1775))
        self.assertEqual(8, flip_bit_optimal(1775))


if __name__ == '__main__':
    unittest.main()