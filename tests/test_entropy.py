import unittest
import math
from src.functions.entropy import entropy


class TestEntropy(unittest.TestCase):
    def test_binary_equal_distribution(self):
        """Test entropy for equal binary distribution [0.5, 0.5]"""
        probabilities = [0.5, 0.5]
        self.assertEqual(entropy(probabilities), 1.0)

    def test_binary_unequal_distribution(self):
        """Test entropy for unequal binary distribution [0.1, 0.9]"""
        probabilities = [0.1, 0.9]
        self.assertAlmostEqual(entropy(probabilities), 0.4689955935892812)

    def test_multi_class_equal_distribution(self):
        """Test entropy for equal distribution with multiple classes [0.33, 0.33, 0.34]"""
        probabilities = [0.33, 0.33, 0.34]
        expected = -(
            0.33 * math.log2(0.33)
            + 0.33 * math.log2(0.33)
            + 0.34 * math.log2(0.34)
        )
        self.assertAlmostEqual(entropy(probabilities), expected, places=6)

    def test_zero_entropy(self):
        """Test entropy for perfect certainty [1.0, 0.0]"""
        probabilities = [1.0, 0.0]
        self.assertEqual(entropy(probabilities), 0.0)

    def test_invalid_probabilities(self):
        """Test that probabilities sum to approximately 1"""
        probabilities = [0.5, 0.6]  # Sum > 1
        with self.assertRaises(ValueError):
            entropy(probabilities)

        probabilities = [0.3, 0.3]  # Sum < 1
        with self.assertRaises(ValueError):
            entropy(probabilities)


if __name__ =main()
