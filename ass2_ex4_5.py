from itertools import product


# Function that checks if the Kraft's inequality is satisfied for a given set of lengths and a base
# Note: Kraft's inequality is met, if it is possible to construct a prefix code with the given lengths and base
def kraft_inequality(lengths, base):
    return sum(base**-length for length in lengths) <= 1


# Function that computes the average length of a code given the lengths and the probabilities of the messages
def average_length(lengths, probabilities):
    return sum(p * l for p, l in zip(probabilities, lengths))


code_alphabet_base = 3
target_average_length = 2.3
probabilities = [1 / 12, 1 / 12, 2 / 12, 2 / 12, 2 / 12, 4 / 12]
count_of_messages = len(probabilities)

max_lengths = [0] * count_of_messages
for i, probability in enumerate(probabilities):
    dummy_lengths = [1] * count_of_messages
    for length in range(1, 20):
        dummy_lengths[i] = length
        if average_length(dummy_lengths, probabilities) > target_average_length:
            max_lengths[i] = length - 1
            break

# Generate all possible length combinations for the given maximum lengths
# and check if the Kraft's inequality is satisfied and the average length is equal to the target average length
for lengths in product(*[range(1, max_length + 1) for max_length in max_lengths]):
    if (
        kraft_inequality(lengths, code_alphabet_base)
        and average_length(lengths, probabilities) == target_average_length
    ):
        # A prefix-free code with the average lenght was found
        print(lengths)
        break
