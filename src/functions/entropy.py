import math
from typing import List


def entropy(class_probabilities: List[float]) -> float:
    """
    Calculate the entropy of a probability distribution using the formula:
    H(X) = -Σ p(x) * log2(p(x))

    Parameters:
    probabilities: A list or array of probabilities that must sum to 1.

    Returns:
    float: The entropy of the distribution.
    """
    terms = []

    # Check that the input sum to 1
    if not math.isclose(sum(class_probabilities), 1.0):
        raise ValueError("The sum of the probabilities must be equal to 1.")

    for each_class_probability in class_probabilities:

        if each_class_probability == 0:
            # If the probability is zero, we skip it to avoid log(0)
            continue

        each_term = -each_class_probability * math.log(
            each_class_probability, 2
        )
        terms.append(each_term)

    # Sum the terms to get the entropy
    entropy_value = sum(terms)

    return entropy_value


if __name__ == "__main__":

    # Test Wrong Inputs
    try:
        # Should raise an error because the sum must be 1
        entropy([0.5, 0.5, 0.1])
    except ValueError as e:
        print(f"Error: {e}")

    # In this example, there are the same amount of probability for each class
    # so the entropy should be maximum (1)
    probabilities = [0.5, 0.5]
    print(f"Entropy: {entropy(probabilities)}")
    assert entropy(probabilities) == 1.0

    # In this example, all the probability is concentrated in one class
    # so the entropy should be minimum (0)
    probabilities = [1.0, 0.0]
    print(f"Entropy: {entropy(probabilities)}")
    assert entropy(probabilities) == 0.0

    # In this example, the probabilities are not equal, so the entropy
    # should be between 0 and 1, and as the probabilities are not too skewed,
    # the entropy should be high
    probabilities = [0.4, 0.6]
    print(f"Entropy: {entropy(probabilities)}")
    assert round(entropy(probabilities), 3) == 0.971

    # In this example, the probabilities are skewed, so the entropy
    # should be lower than the previous example
    probabilities = [0.1, 0.9]
    print(f"Entropy: {entropy(probabilities)}")
    assert entropy(probabilities) == 0.4689955935892812
